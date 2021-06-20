# 简介

`account` 命令用来设置当前用户的 `AccessKey` 和 `SecretKey` ，这对 Key 主要用在其他的需要授权的命令中，比如 `stat` , `delete` , `listbucket` 命令中。
该命令设置的信息，经过加密保存在 HOME 目录下的 `.qcommand/account.json` 文件中。

本地数据库会记录 `account` 注册的所有 <AccessKey> ,  <SecretKey>  和 <Name> 的信息。
# 格式

```
qcommand account
``` 

打印当前设置的`AccessKey`, `SecretKey`和`Name`

```
qcommand account <Your AccessKey> <Your SecretKey> <Your Account Name>
``` 

设置当前用户的`AccessKey`, `SecretKey`和`Name`, Name是用户可以任意取的名字，表示当前在本地记录的账户的名称，和在七牛注册的邮箱信息没有关系。

# 参数

|参数名|描述|
|--------|--------|
|AccessKey|七牛账号对应的AccessKey [获取](https://portal.qiniu.com/user/key)|
|SecretKey|七牛账号对应的SecretKey [获取](https://portal.qiniu.com/user/key)|
|Name|账户的名字, 可以任意取，和在七牛注册的邮箱信息没有关系， 只是qcommand本地用来标示<ak, sk>对 |

# 示例

1.设置当前用户的AccessKey, SecretKey, Name

```
qcommand account ELUs327kxVPJrGCXqWae9yioc0xYZyrIpbM6Wh6x LVzZY2SqOQ_I_kM1n00ygACVBArDvOWtiLkDtKiw name_test
```

2.输出当前用户设置的AccessKey和SecretKey

```
qcommand account
```
输出:

```
Name: name_test
AccessKey: ELUs327kxVPJrGCXqWae9yioc0xYZyrIpbM6Wh6x
SecretKey: LVzZY2SqOQ_I_kM1n00ygACVBArDvOWtiLkDtKiw
```

3. 我们可以在设置name_test账户后，继续添加一个账户

```
qcommand account ELUs327kxVPJrGCXqWae9yioc0xYZyrIpbM6abc LVzZY2SqOQ_I_kM1n00ygACVBArDvOWtiLkDthaha name_test2
```
qcommand 可以记录多个设置的账户信息，账户的管理，切换，删除等，可以参考qcommand user命令[文档](docs/user.md)
