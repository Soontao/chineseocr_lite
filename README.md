> 本项目基于[chineseocr](https://github.com/chineseocr/chineseocr) 与[psenet](https://github.com/WenmuZhou/PSENet.pytorch)  实现中文自然场景文字检测及识别

![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/theosun/chineseocr_lite)
![GitHub](https://img.shields.io/github/license/Soontao/chineseocr_lite)

## 环境

- pytorch  1.2.0 
- python3
- linux/macos/windows
- windows环境配置参考热心网友的文章[Python构建快速高效的中文文字识别OCR](https://blog.csdn.net/lly1122334/article/details/104752851) 👍

## PSENET 编译

``` Bash
cd psenet/pse
rm -rf pse.so 
make 
```

## web服务启动

```bash
# 8080端口号，可以设置任意端口
python app.py 8080 
```

## 访问服务

http://127.0.0.1:8080/ocr

## 实现功能

- [x]  提供轻量的backone检测模型psenet（8.5M）,crnn_lstm_lite(9.5M) 和行文本方向分类网络（1.5M）
- [x]  任意方向文字检测，识别时判断行文本方向 
- [x]  crnn\crnn_lite lstm\dense识别（ocr-dense和ocr-lstm是搬运[chineseocr](https://github.com/chineseocr/chineseocr)的）   
- [x]  支持竖排文本识别  
- [x]  ncnn 实现 (支持lstm) nihui大佬实现的[crnn_lstm推理](https://github.com/ouyanghuiyu/chineseocr_lite/pull/41) 具体操作详解: [详细记录超轻量中文OCR LSTM模型ncnn实现](https://zhuanlan.zhihu.com/p/113338890?utm_source=qq&utm_medium=social&utm_oi=645149500650557440)
- [x]  提供竖排文字样例以及字体库（旋转90度的字体）
- [ ]  mnn  实现 

### 2020.03.16更新

- psenet ncnn核扩展实现，有效解决粘连文本检测问题，详见[ncnn ocr一条龙](https://github.com/ouyanghuiyu/chineseocr_lite/tree/master/ncnn_project/ocr)
- nihui大佬实现的[crnn_lstm推理](https://github.com/ouyanghuiyu/chineseocr_lite/pull/41) 具体操作详解: [详细记录超轻量中文OCR LSTM模型ncnn实现](https://zhuanlan.zhihu.com/p/113338890?utm_source=qq&utm_medium=social&utm_oi=645149500650557440)

### 2020.03.12更新

- 升级crnn_lite_lstm_dw.pth模型crnn_lite_lstm_dw_v2.pth , 精度更高

## 参考
1. ncnn  https://github.com/Tencent/ncnn         
2. crnn  https://github.com/meijieru/crnn.pytorch.git              
3. chineseocr  https://github.com/chineseocr/chineseocr      
4. Psenet https://github.com/WenmuZhou/PSENet.pytorch  
5. 语言模型实现 https://github.com/lukhy/masr
