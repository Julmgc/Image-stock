## <font size="7">**Image stock**</font>

​​### <font color="gree"> API that uploads, saves and downloads images(png, jpg and gif format) in server folder(disk) </font> Saves a movie

## <font size="6">Base URL </font>

## <font size="6">Routes</font>

​
​

### <font color="purple"> POST </font> Post an image file, in the JPG, PNG or GIF format, maximun 1MB**\***

​

```json
/upload
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "lugarcerto.jpg"
}
```

​

### <font color="purple"> GET </font> List of all files names

​

```json
/files
```

```json
{
  "lugarcerto.jpg"
  "Shakespeare.jpg"
  "psicoterapia-1.jpg"
}
```

​

### <font color="purple"> GET </font> List of files by type(JPG, PNG or GIF)

​

```json
/files/<string:type>
```

​

```json
{
  "lugarcerto.jpg"
  "Shakespeare.jpg"
  "psicoterapia-1.jpg"
}
```

### <font color="purple"> GET </font> Download specific file(ex: Shakespeare.jpg)

​

```json
/download/<path:file_name
```

### <font color="purple"> GET </font> Download zip file of specific image format(png, jpg or gif) and compresstion ratio(1 until 9)

​

```json
/download-zip?file_extension=jpg&compression_ratio=1
```
