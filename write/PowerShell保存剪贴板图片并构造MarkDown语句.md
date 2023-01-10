### 原生命令
```powershell
$list = (Get-ClipBoard) -like '*err*'
```

这里有一个原生命令，`Set-Clipboard` 以及`Get-Clipboard`  所以保存文件只需要两步
```powershell
$PNGfile=Get-Clipboard -Format Image
$PNGfile.Save($file)
```
### 小技巧
针对对象输出的屏幕字符，可以先转换成字符串，然后输出到剪贴板
```
dir | Out-String | Set-Clipboard 
```

### .net方法
PowerShell对文件的操作进行创建修改是比较简单的
```powershell
$img = [Windows.Clipboard]::GetImage()
```
根据这个关键字，我们看一下  `Clipboard Class`

| GetImage() | Returns a BitmapSource object from the Clipboard that contains data in the Bitmap format. |
| ---------- | ----------------------------------------------------------------------------------------- |

这里不光可以get，还可以set，不光是图片，文字音频都可以操作，算是针对剪贴板的一整套方案都有了。原文输出的格式是PNG的，我想试试如何输出JPG

#### 剪贴板保存PNG
```powershell
#剪贴板直接保存png
Add-Type -Assembly PresentationCore
$img = [Windows.Clipboard]::GetImage()
if ($null -eq $img ) {
  Write-Host "剪贴板无图"
  Exit
}
$fcb = New-Object Windows.Media.Imaging.FormatConvertedBitmap($img, [Windows.Media.PixelFormats]::Rgb24, $null, 0)
$filename = ((Get-Date -f s) -replace '[-T:]', '')
$file = "c:/img/{0}.jpg" -f $filename
Write-Host ("`n 找到图片. {0}x{1} 像素，保存到{2}`n" -f $img.PixelWidth, $img.PixelHeight, $file)
$stream = [IO.File]::Open($file, "OpenOrCreate")
$encoder = New-Object Windows.Media.Imaging.PngBitmapEncoder
$encoder.Frames.Add([Windows.Media.Imaging.BitmapFrame]::Create($fcb))
$encoder.Save($stream)
# $stream.Dispose()
```
#### 各种花式，不局限于PowerShell
```powershell
{
    Bitmap bmp1 = new Bitmap(typeof(Button), "Button.bmp");
    bmp1.Save(@"c:\button.png", ImageFormat.Png);
}
```
- [相对简单存储图片]( https://stackoverflow.com/questions/41665/bmp-to-jpg-png-in-c-sharp)
- [高级存储图片](https://stackoverflow.com/questions/1484759/quality-of-a-saved-jpg-in-c-sharp)
- [官方例子](https://docs.microsoft.com/en-us/dotnet/api/system.drawing.imaging.imagecodecinfo.getimageencoders?view=netframework-4.8)

#### PNG转换JPG

这里用到了一个技巧，就是 `Add-Type -AssemblyName system.drawing`

```powershell
    Add-Type -AssemblyName system.drawing
    $Source=“C:\img\tt2.png”
    $imageFormat = "System.Drawing.Imaging.ImageFormat" -as [type]
    $image = [drawing.image]::FromFile($Source)
    # 创建新图像
    $NewImage = [System.Drawing.Bitmap]::new($Image.Width,$Image.Height)
    $NewImage.SetResolution($Image.HorizontalResolution,$Image.VerticalResolution)
    #根据新图像添加图形
    $Graphics = [System.Drawing.Graphics]::FromImage($NewImage)
    $Graphics.Clear([System.Drawing.Color]::White) # Set the color to white
    $Graphics.DrawImageUnscaled($image,0,0) # Add the contents of $image
    #存储
    $NewImage.Save("c:\img\vvv.jpg",$imageFormat::Jpeg)
```

#### 读取一个IMG，调整大小，以及写入

```powershell
Add-Type -AssemblyName System.Drawing 
$img = New-Object System.Drawing.Bitmap(96, 96) 
([System.Drawing.Graphics]::FromImage($img)).DrawImage([System.Drawing.Image]::FromFile((Get-Item C:\img\20191104135629.jpg)), 0, 0, 128, 128) 
$jpegCodecInfo = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | where {$_.MimeType -eq 'image/jpeg'} $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1) 
$encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, 90) 
$img.Save("c:\img\bouska2.jpg", $jpegCodecInfo, $encoderParams) 
$img.Dispose() 
```

#### 剪贴板直接保存png，然后传到github上，引用github page的地址

```powershell
#剪贴板直接保存png
Add-Type -Assembly PresentationCore
$img = [Windows.Clipboard]::GetImage()
if ($null -eq $img ) {
  Write-Host "剪贴板无图"
}
$rootpath="C:/kukisama.github.io/picupdate/"
$fcb = New-Object Windows.Media.Imaging.FormatConvertedBitmap($img, [Windows.Media.PixelFormats]::Rgb24, $null, 0)
$filename = ((Get-Date -f s) -replace '[-T:]', '')
$file = "$rootpath{0}.png" -f $filename
Write-Host ("`n 找到图片. {0}x{1} 像素，保存到{2}`n" -f $img.PixelWidth, $img.PixelHeight, $file)
$stream = [IO.File]::Open($file, "OpenOrCreate")
$encoder = New-Object Windows.Media.Imaging.PngBitmapEncoder
$encoder.Frames.Add([Windows.Media.Imaging.BitmapFrame]::Create($fcb))
$encoder.Save($stream)
$stream.Dispose()
$rootpath="C:/kukisama.github.io/picupdate/"
cd $rootpath
cd ..
$lastfile=(ls $rootpath |sort LastWriteTime  -Descending)[0].name
$MARKDOWNpic=New-Object System.Collections.ArrayList
$MARKDOWNpic.add('![image](http://github.ny9s.com/picupdate/'+$lastfile+')')|out-null
$MARKDOWNpic.Add(' ')|out-null
$MARKDOWNpic|Set-Clipboard
Write-Host "盆友，现在可以在MarkDown编辑器里面复制文本地址了"
git add $rootpath$lastfile
git commit -m $lastfile
git push -u origin master|Out-Null -ErrorAction SilentlyContinue
#git  rm -r C:/kukisama.github.io/picupdate/
```
### Reference
[PowerShell保存剪贴板图片并构造MarkDown语句][1]  
[PowerShell使用剪贴板传递数据和结果][2]

[1]:https://www.yisu.com/zixun/12904.html
[2]:https://www.pstips.net/using-clipboard-to-transfer-data-and-results.html