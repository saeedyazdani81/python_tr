### برنامه ی scan_numbers را برای رسیدن به امکانات زیر توسعه دهید

### در برنامه scan_numbers دوره تناوب برای مقدار 3 ثابت بود
### میخواهیم در این برنامه
### مقدار دوره تناوب (period) را خود کاربر تعیین کند.
#
### بجای نمایش اعداد پیمایش شده میانگین آنها را درون لیستی قرار داده و در انتها لیست جدید که حاصل میانگین های بدست آمده از پیمایش با دوره ی تناوب مشخص است را نمایش دهد
### برای نمونه 

```python
# لیست اعداد
numbers = [1,2,3,21,51,68,59,53,654,21,57]
```
#
###  وضعیتی که در برنامه ی scan_numbers با دوره تناوب 3 برای خروجی داشتیم:
#### [1, 2, 3]
#### [2, 3, 21]
#### [3, 21, 51]
#### [21, 51, 68]
#### [51, 68, 59]
#### [68, 59, 53]
#### [59, 53, 654]
#### [53, 654, 21]
#### [654, 21, 57]
#
#### نکته: طبیعتا اگر کاربر دوره ی تناوب را مقداری بجز 3 انتخاب کند خروجی ها هم متفاوت خواهند بود
#### نکته: دوره تناوب باید عددی بین 1 و طول لیست باشد.
#
### وضعیت خروجی برای برنامه ی فعلی با دوره تناوب 3 بصورت زیر خواهد بود:
### [2.0, 8.67, 25.0, 46.67, 59.33, 60.0, 255.33, 242.67, 244.0]
### در این خروجی عنصر اول یعنی 2.0  حاصل میانگین اعداد زیر است:
#### [1, 2, 3]
### و عصنر دوم یعنی 8.67 حاصل میانگین اعداد زیر است:
#### [2, 3, 21]
### و بهمین ترتیب تا انتها ادامه خواهد داشت
#
#### شما با حل کردن این برنامه موفق به نحوه محاسبه میانگین متحرک نمایی شده اید که در امور مالی و تحلیل تکنیکال کاربرد فراوانی دارد.
#### اطلاعات بیشتر:
#### [آشنایی با میانگین متحرک ساده در تحلیل تکنیکال](https://www.cheragh.com/blog/%D8%A2%D8%B4%D9%86%D8%A7%DB%8C%DB%8C-%D8%A8%D8%A7-%D9%85%DB%8C%D8%A7%D9%86%DA%AF%DB%8C%D9%86-%D9%85%D8%AA%D8%AD%D8%B1%DA%A9-%D8%B3%D8%A7%D8%AF%D9%87-%D8%AF%D8%B1-%D8%AA%D8%AD%D9%84%DB%8C%D9%84-%D8%AA%DA%A9%D9%86%DB%8C%DA%A9%D8%A7%D9%84/#:~:text=%D8%AF%D8%B1%20%D9%88%D8%A7%D9%82%D8%B9%20%D9%85%DB%8C%D8%A7%D9%86%DA%AF%DB%8C%D9%86%20%D9%85%D8%AA%D8%AD%D8%B1%DA%A9%20%D8%B3%D8%A7%D8%AF%D9%87,%D8%A8%D8%B1%20X%20%D9%85%D8%AD%D8%A7%D8%B3%D8%A8%D9%87%20%D8%AE%D9%88%D8%A7%D9%87%D8%AF%20%D8%B4%D8%AF.)

#### [Understanding Simple Moving Average (SMA)](https://www.investopedia.com/terms/s/sma.asp#:~:text=A%20simple%20moving%20average%20(SMA)%20is%20an%20arithmetic%20moving%20average,periods%20in%20the%20calculation%20average.)