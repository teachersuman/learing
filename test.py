from MyQR import myqr


url = 'https://www.baidu.com/'
version, level, qr_name = myqr.run(
    words=url,
    version=2,
    contrast=1.0,
    level='H',
    picture='ty.gif',
    colorized=True,
    brightness=1.0,
    save_name='ty1.gif'
)

