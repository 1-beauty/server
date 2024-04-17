# from transformers import BertTokenizer, BertModel
# import torch
#
#
# # 判断两个句子的相似度
# def is_same_thing_bert(sentence1, sentence2, threshold=0.75):
#     # 初始化模型和分词器
#     tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
#     model = BertModel.from_pretrained('bert-base-chinese')
#
#     # 分词并编码句子
#     inputs = tokenizer([sentence1, sentence2], return_tensors='pt', padding=True, truncation=True)
#
#     # 通过模型获取句子的嵌入向量
#     with torch.no_grad():
#         outputs = model(**inputs)
#
#     # 使用平均池化获取句子的嵌入表示
#     embeddings = outputs.last_hidden_state.mean(dim=1)
#
#     # 计算余弦相似度
#     cos = torch.nn.CosineSimilarity(dim=0)
#     similarity = cos(embeddings[0], embeddings[1]).item()
#
#     # 判断是否相同
#     return similarity > threshold
#
#
# # 示例
# sentence1 = "拜登称不支持以色列反击"
# sentence2 = "拜登：美国不会支持以色列反击行动"
# print(is_same_thing_bert(sentence1, sentence2))  # 输出：True
