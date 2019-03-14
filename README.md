### My Scripts

English | [中文](#中文)

This repositories is builded to collect scripts/spiders used in my daily work and life. It doesn't contain advanced technology or knowledge. But they really solve my problems and reduce my workload. The porcess of writing these little programs made me fall in love with Python. 

If you have any problems about the code or comments please contact me at lyhdut@163.com. I will be very happy if my litte programs help you. 

+ [bidding_result.py](./bid_result.py) - Craw the latest result of bidding from[宁波公共资源交易中心](http://www.bidding.gov.cn/zhdh.jhtml) and use tesseract to detect text. if win the bidding, use wxpy send Wechat message.

+ [photo operation](./photo) - Organize photos by EXIF(Exchangeable Image File Format) information.
    + [photo_orginaze_bydate.py](./photo/photo_orginaze_bydate.py) - According datetime of photos under the given folder, These photos will be moved to the corresponding folder. The file directory tree structure is Year/Month/Day/.

    + [photo_location.py](./photo/photo_location.py) - Locating the exact location of the photo by GPS information .

    + [photo_rename_bydate.py](./photo/photo_rename_bydate.py) - Rename photos under the given folder by DateTime information, which is got from EXIF.

+ [pdf operation](./pdf): PDF file operation, including merging PDF files under the given folder, inserting, deleting specified page.

    + [pdf_merge.py](./pdf/pdf_merge.py) - Merge PDF files under the given folder.

    + [pdf_insert.py](./pdf/pdf_insert.py) - Insert another PDF file at the given location.

    + [pdf_delete.py](./pdf/pdf_delete.py) - Delete the given page.  


##### 中文

这个repo用来收集我日常生活中用到的自动化脚本/爬虫。虽然都是一些很小的项目，但确实解决了我生活工作中的一些问题，提高了工作效率、节省了大量时间。同时在写这些小脚本的过程中我深深地喜欢上了Python。

有问题或者建议的话，欢迎跟我联系lyhdut@163.com。如果这些脚本有帮助到你，我会很开心哒。

+ [bidding_result.py](./bid_result.py) - 爬取宁波公共资源交易中心最新中标结果，用tesseract识别结果图， 若中标(中标单位与给出中标单位一致)则调用wxpy发送微信消息。

+ [photo operation](./photo) - 利用照片的EXIF(可交换图像文件格式)信息整理照片。
    + [photo_orginaze_bydate.py](./photo/photo_orginaze_bydate.py)：将照片按照拍摄时间分别移动到相应的文件夹，文件夹树形结构为 Year/Month/Day/。

    + [photo_location.py](./photo/photo_location.py): 通过获取图片EXIF中的GPS信息来定位具体拍摄地点。

    + [photo_rename_bydate.py](./photo/photo_rename_bydate.py): 通过获取图片EXIF中的拍摄时间信息重命名，重命名格式为"拍摄时间+原名"。

+ [pdf operation](./pdf): PDF文件操作，包括合并指定文件夹下PDF文件，插入、删除、替换指定页码文件等。

    + [pdf_merge.py](./pdf/pdf_merge.py): 合并指定文件夹下的PDF文件。

    + [pdf_insert.py](./pdf/pdf_insert.py): 在PDF文件指定页码位置插入另一PDF文件。

    + [pdf_delete.py](./pdf/pdf_delete.py): 删除PDF文件中指定页码。