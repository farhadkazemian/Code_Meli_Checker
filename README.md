# Code_Meli_Checker
Iran Residential ID Number Checker
<html dir="rtl">

<head>
<meta name="keywords" content="تشخیص صحت کد ملی, کد ملی , الگوریتم تشخیص ">
<meta name="description" content="تشخیص صحت کد ملی- کد ملی - الگوریتم تشخیص ">
<link rel="stylesheet" type="text/css" href="../../stylesheet/mystyles.css">

</head>

<body>
	<a href="https://www.aparat.com/v/FyjSV/">مشاهده ویدیو در آپارات</a>
<div align="center">
  
  <table border="1" DIR=rtl cellpadding="0" cellspacing="1" style="border-collapse: collapse; text-align: justify; direction: rtl; text-indent: 5; margin-left: 15; margin-right: 12" width="750" dir="rtl" id="table5">
    <tr>
      <td bgcolor="#3973AC" height="52">
      <p style="text-align: center"><font color="#FFFFFF"><b><span lang="fa">تشخیص صحت کد ملی</span></b></font></td>
    </tr>
    <tr>
      <td height="52">
      <span lang="fa">امروزه در اکثر نرم افزارهای تولیدی نیاز به استفاده از کد ملی 
به عنوان یک مشخصه منحصر به فرد برای اطلاعات فردی می باشد.</span><p><span lang="fa">از طرفی متاسفانه در حال حاضر هیچ الگوریتمی برای تشخیص صحت کد 
ورودی در اختیار برنامه نویسان وجود ندارد.</span></p>
<p><span lang="fa">اخیرا با توجه به نیاز خودم به کنترل صحت کد ورودی الگوریتم 
مربوط به کنترل صحت کد ملی را بدست آوردم و چون مطمئن هستم افراد زیادی هم همین نیاز 
را دارند روال انجام کار را در این مقال توضیح می دهم</span></p>
<p>کد ملی شماره ای است 10 رقمی که از سمت چپ سه رقم کد شهرستان محل صدور شناسنامه ، 
شش رقم بعدی کد منحصر به فرد برای فرد دارنده شناسنامه در شهرستان محل صدرو و رقم آخر آن هم یک رقم کنترل است که 
از روی 9 رقم سمت چپ بدست می آید. برای بررسی کنترل کد کافی است مجدد از روی 9 رقم 
سمت چپ رقم کنترل را محاسبه کنیم</p>
<p><span lang="fa"> 
ساختار کد ملی در زیر نشان داده شده است:</span></p>
<div align="center">
	<table border="1" width="300" dir="rtl" style="border-collapse: collapse" bordercolor="#808080">
		<tr>
			<td colspan="11" align="center" style="text-align: center">
			<p style="text-align: center">ساختار کد ملی</td>
		</tr>
		<tr>
			<td align="center" style="text-align: center">ارقام کد</td>
			<td align="center" style="text-align: center">رقم کنترل</td>
			<td colspan="9" align="center" style="text-align: center">9 رقم سمت چپ کد ملی</td>
		</tr>
		<tr>
			<td align="center" style="text-align: center">موقعیت</td>
			<td align="center" style="text-align: center">
			<p style="text-align: center">1</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">2</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">3</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">4</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">5</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">6</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">7</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">8</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">9</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">10</td>
		</tr>
		<caption>&nbsp;</caption>
	</table>
</div>
<p>1- برای محاسبه رقم کنترل از روی سایر ارقام ، هر رقم را در موقعیت آن ضرب کرده 
و حاصل را با هم جمع می کنیم.</p>
<p>2- مجموع بدست آمده از مرحله یک را بر 11 تقسیم می کنیم</p>
<p>3- اگر باقیمانده کمتر از 2 باشد ، رقم کنترل باید برابر باقیمانده باشد در غیر 
اینصورت رقم کنترل باید برابر یازده منهای باقیمانده باشد</p>
<p>مثال : آیا کد 7731689951 یک کد ملی معتبر است؟</p>
<p>برای این منظور کد</p>
<div align="center">
	<table border="1" width="427" dir="rtl" style="border-collapse: collapse" bordercolor="#808080">
		<tr>
			<td colspan="11" align="center" style="text-align: center">ساختار کد ملی</td>
		</tr>
		<tr>
			<td align="center" style="text-align: center">ساختار کد</td>
			<td align="center" style="text-align: center">رقم کنترل</td>
			<td colspan="9" align="center" style="text-align: center">9 رقم سمت چپ کد ملی</td>
		</tr>
		<tr>
			<td align="center" style="text-align: center">ارقام کد</td>
			<td align="center" style="text-align: center">1</td>
			<td align="center" style="text-align: center">5</td>
			<td align="center" style="text-align: center">9</td>
			<td align="center" style="text-align: center">9</td>
			<td align="center" style="text-align: center">8</td>
			<td align="center" style="text-align: center">6</td>
			<td align="center" style="text-align: center">1</td>
			<td align="center" style="text-align: center">3</td>
			<td align="center" style="text-align: center">7</td>
			<td align="center" style="text-align: center">7</td>
		</tr>
		<tr>
			<td align="center" style="text-align: center">موقعیت</td>
			<td align="center" style="text-align: center">1</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">2</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">3</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">4</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">5</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">6</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">7</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">8</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">9</td>
			<td align="center" style="text-align: center" bgcolor="#9999FF">10</td>
		</tr>
		<tr>
			<td align="center" style="text-align: center">محاسبه حاصل ضرب</td>
			<td align="center" style="text-align: center">&nbsp;</td>
			<td align="center" style="text-align: center">10</td>
			<td align="center" style="text-align: center">27</td>
			<td align="center" style="text-align: center">36</td>
			<td align="center" style="text-align: center">40</td>
			<td align="center" style="text-align: center">36</td>
			<td align="center" style="text-align: center">7</td>
			<td align="center" style="text-align: center">24</td>
			<td align="center" style="text-align: center">63</td>
			<td align="center" style="text-align: center">70</td>
		</tr>
		<caption>&nbsp;</caption>
	</table>
	<p align="right">حاصل<span lang="en-us"> </span>جمع ضرب ارقام 2 الی 10 را در موقعیت آنها محاسبه می کنیم</p>
	<p align="left" dir="ltr">7*10+7*9+3*8+1*7+6*6+8*5+9*4+9*3+5*2=313</p>
	<p align="left" dir="ltr">313<font face="Times New Roman"><span lang="en">÷</span>11=28 
	و <span lang="en-us">R=5</span></font></p>
	<p align="right">چون باقیمانده برابر 5 و بزرگتر مساوی 2 است پس باید رقم 
	کنترل این کد برابر 6 ( یازده منهای 5 برابر 6 
	)باشد. </p>
	<p align="right">با دقت در کد متوجه می شویم که رقم کنترل ورودی برابر 1 است 
	پس کد مورد نظر به عنوان یک کد معتبر قابل قبول نیست<span lang="en-us">.</span></p>

  </table>
</div>
<p>&nbsp;</p>
<div align="center">
	<p align="right">&nbsp;</p>
	<p>&nbsp;</div>

</body>

</html>
