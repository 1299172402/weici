# 表中 detail 的各个属性


| 是否需要 | 属性                 | 释义         | 备注                                                 |
| -------- | -------------------- | ------------ | ---------------------------------------------------- |
| 0        | id                   | 词id         | 数据库中的词汇id                                     |
| 1        | word                 | 单词/词组    |                                                      |
| 1        | part_of_speech       | 词性         | 如 adj，n                                            |
| 1        | en_phonetic_symbols  | 英音英标     |                                                      |
| 1        | en_file              | 英音发音文件 |                                                      |
| 1        | usa_phonetic_symbols | 美音音标     |                                                      |
| 1        | usa_file             | 美音发音文件 |                                                      |
| 0        | speech               |              | 未知的音频文件（不在下载里面）                       |
| 1        | lv_speak             | 口语         |                                                      |
| 1        | lv_write             | 书面         |                                                      |
| 1        | lv_read              | 阅读         |                                                      |
| 1        | lv_frequency         | 词频         |                                                      |
| 1        | point                |              | 是否为重难点词汇，类型int                            |
| 0        | point_name           |              | 0：否；1：是                                         |
| 0        | not_use              |              | 未知                                                 |
| 0        | not_use_name         |              | 未知                                                 |
| 0        | outpoint             |              | 是否为额外词汇，类型int                              |
| 0        | outpoint_name        |              | 0：无；1：课标外词汇；2：课标派词汇                  |
| 1        | use_method           | 用法点拨     |                                                      |
| 1        | antonym              | 反义词       |                                                      |
| 1        | synonyms             | 近义词       |                                                      |
| 1        | family_word          | 词族         |                                                      |
| 0        | family_word_image    |              |                                                      |
| 0        | rate                 |              | 未知，类型int，从0开始，测试到24仍有，有部分数字没有 |
| -1       | area                 | 地区         | 如 苏、津                                            |
| -1       | book                 |              | 类型int                                              |
| -1       | book_name            |              | 类型str，如"Book 1"                                  |
| -1       | unit                 |              | 类型int                                              |
| -1       | unit_name            |              | 类型str，如"Unit 2"                                  |
| -1       | fixed_id             |              | 似乎全部为0                                          |
| -1       | simple               |              | 如"B1U2"                                             |
| -1       | follow_word          |              | 感觉就是当前词                                       |
|          | new_attribute        |              | 未知                                                 |
| 1        | gy_paraphrase        | 英文释义     |                                                      |
| 1        | gy_fixed_collocation | 固定搭配     |                                                      |
| 1        | gy_derivative        | 派生词汇     |                                                      |
| 1        | gy_exam_link         | 真题解析     |                                                      |
|          | gy_word_expand       |              |                                                      |

是否需要中：

| 值   | 释义       |
| ---- | ---------- |
| -1   | 完全不需要 |
| 0    | 不太需要   |
| 1    | 需要       |

