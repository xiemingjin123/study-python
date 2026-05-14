import math

from torch import nn
import config
import torch
class PositionEncoding(nn.Module):
    def __init__(self, d_model, max_len=500):
        super().__init__()
        self.d_model = d_model
        self.max_len = max_len

        pos = torch.arange(0, self.max_len, dtype=torch.float).unsqueeze(1)  # pos.shape: (max_len, 1)
        _2i = torch.arange(0, self.d_model, step=2, dtype=torch.float)  # _2i.shape: (d_model/2,)
        div_term = torch.pow(10000, _2i / self.d_model)
        sins = torch.sin(pos / div_term)  # sins.shape: (max_len, d_model/2)
        coss = torch.cos(pos / div_term)  # coss.shape: (max_len, d_model/2)

        pe = torch.zeros(self.max_len, self.d_model, dtype=torch.float)  # pe.shape: (max_len, d_model)

        pe[:, 0::2] = sins
        pe[:, 1::2] = coss

        self.register_buffer('pe', pe)

    def forward(self, x):
        seq_len = x.size(1)
        return x + self.pe[:seq_len]



class TranslationModel(nn.Module):
    def __init__(self,zh_vocab_size,en_vocab_size,zh_padding_index,en_padding_index):
        super().__init__()
        self.zh_embedding = nn.Embedding(num_embeddings=zh_vocab_size,embedding_dim=config.DIM_MODEL,padding_idx=zh_padding_index)
        self.en_embedding = nn.Embedding(num_embeddings=en_vocab_size,embedding_dim=config.DIM_MODEL,padding_idx=en_padding_index)
        self.position_encoding = PositionEncoding(config.MAX_SEQ_LENGTH,config.DIM_MODEL)
        self.transform = nn.Transformer(d_model=config.DIM_MODEL,nhead=config.NUM_HEADS,num_encoder_layers=config.NUM_ENCODER_LAYERS,num_decoder_layers=config.NUM_DECODER_LAYERS)
        self.linear = nn.Linear(in_features=config.DIM_MODEL,out_features=en_vocab_size)

    def encode(self,src,src_pad_mask):
        embed = self.zh_embedding(src)
        position = self.position_encoding(embed)
        memory = self.transform.encoder(src=position,src_key_padding_mask=src_pad_mask)
        return memory

    def decode(self,tgt,memory,tgt_mask,memory_pad_mask):
        embed = self.en_embedding(tgt)
        embed = self.position_encoding(embed)
        output = self.transform.decoder(tgt=embed,memory=memory,tgt_mask=tgt_mask,memory_key_padding_mask=memory_pad_mask)
        output = self.linear(output)
        return output

    def forward(self,src,src_pad_mask,tgt,tgt_mask):
        memory = self.encode(src=src,src_pad_mask=src_pad_mask)
        output = self.decode(tgt=tgt,memory=memory,tgt_mask=tgt_mask,memory_pad_mask=src_pad_mask)
        return output
