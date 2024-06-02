fallMenuTranslateX=window.innerWidth;
document.getElementById('fallMenu').style.transform='translateX(-'+fallMenuTranslateX+'px)';
if(document.querySelector('.globalVar_sumbit').innerHTML==1)
{
	document.getElementById('error1').style.display='block';
	fallMenu('reg');
}
if(document.querySelector('.globalVar_sumbit').innerHTML==2)
{
	document.getElementById('error2').style.display='block';
	fallMenu('log');
}
function fallMenu(value)
{
	const fallMenu=document.getElementById('fallMenu');
	const fallMenuIframe=document.querySelector('.fallMenu_iframe');

	const text1=document.querySelector('.fallMenu_iframe_text1');
	const text2=document.querySelector('.fallMenu_iframe_text2');
	const button1=document.querySelector('.fallMenu_iframe_button1');
	const button2=document.querySelector('.fallMenu_iframe_button2');
	const error1=document.getElementById('error1');
	const error2=document.getElementById('error2');

	if(value=='log')
	{
		fallMenu.style.transform='translateX(0)';
		fallMenuIframe.style.left='510px';
		text1.style.left='-420px';
		button1.style.left='-420px';
		error1.style.left='-500px';
		text2.style.left='80px';
		button2.style.left='80px';
		error2.style.left='0';
	}
	if(value=='reg')
	{
		fallMenu.style.transform='translateX(0)';
		fallMenuIframe.style.left='10px';
		text2.style.left='580px';
		button2.style.left='580px';
		error2.style.left='500px';
		text1.style.left='80px';
		button1.style.left='80px';
		error1.style.left='0';
	}
	if(value=='close')
	{
		fallMenu.style.transform='translateX(-'+fallMenuTranslateX+'px)';
	}
}