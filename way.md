从文件中找到 weici_ext.db 导出 fb_word_detail 到 json

如果导出过程中产生问题
e.g.

```
    {
      "id": "47",
      "word": "cab",
      "part_of_speech": "n",
      "detail_json": "{\"id\":47,\"word\":\"cab\",\"part_of_speech\":\"n\",\"en_phonetic_symbols\":\"kæb\",\"en_file\":\"cab-B.aac\",\"usa_phonetic_symbols\":\"kæb\",\"usa_file\":\"cab.aac\",\"speech\":\"\",\"lv_speak\":0,\"lv_write\":0,\"lv_read\":0,\"lv_frequency\":1,\"point\":0,\"point_name\":\"否\",\"not_use\":1,\"not_use_name\":\"是\",\"outpoint\":0,\"outpoint_name\":\"无\",\"use_method\":\"[C]\",\"antonym\":\"\",\"synonyms\":\"\",\"family_word\":\"\",\"family_word_image\":\"\",\"rate\":0,\"area\":\"\",\"book\":1,\"book_name\":\"Book 1\",\"unit\":2,\"unit_name\":\"Unit 2\",\"fixed_id\":0,\"simple\":\"B1U2\",\"follow_word\":\"cab\",\"new_attribute\":1,\"gy_paraphrase\":[{\"id\":1,\"word_id\":47,\"fixed_word_id\":0,\"derivative_id\":0,\"translate_frequency\":0,\"frequency_name\":\"\",\"part_of_speech\":\"\",\"use_method\":\"\",\"chinese\":\"出租车\",\"english\":\"\",\"antonym\":\"\",\"synonyms\":\"\",\"description\":\"\",\"gy_sentential_form\":[],\"gy_example\":[],\"gy_notes\":[],\"gy_biscrimination\":[],\"gy_fixed_collocation\":[]}],\"gy_fixed_collocation\":[],\"gy_derivative\":[],\"gy_exam_link\":[],\"gy_word_expand\":[]}"
    },
```
step.1

 > "detail_json": "{\
 
 替换为
 
 >  "detail_json": {\
 
 
 step.2
 
 detail_json 的末尾也要替换
 
 > }"
 
 > }
 
 step.3
 
 ```\\``` 替换为  ```\```

因为它本来就有一些转义字符```\r``` ```\n``` 之类的 导出时有多了一个\

不处理的话可能使json不是正确的格式
