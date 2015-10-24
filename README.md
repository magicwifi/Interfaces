# 流程 (图）


![gpstrackerandroid](http://7xjtgq.com1.z0.glb.clouddn.com/interface.png)



* 无需医生侧开发任何接口
* 用户侧保留医生基本的元数据（姓名，费用，医生页面url等），通过写操作接口与医生侧同步
* 咨询信息提交，交费在用户侧完成
* 用户侧向医生侧提供待诊病人列表，个人详细咨询信息，个人病历信息等
* 医生侧对上述信息进行展现
* 医生侧调用用户侧的回复接口创建reply接口，实现对病人的回复
* 用户侧对医生回复信息进行展现


# 对外接口（写操作） 
## doctor
 
创建路径: Post /doctors

参数说明 

* id: 医生主键
* name：医生姓名
* avatar：头像路径
* main_desc: 简要说明
* url: 主页地址
* price: 单价

测试程序 python create_doctor.py  23  Jack

返回值：

* {result：200} 调用成功
* {result：400} 调用失败


更新路径：

* Post /:doctor_id/update_doctor_avatar	修改头像
* Post /:doctor_id/update_doctor_url	修改主页
* Post /:doctor_id/update_main_desc	修改说明
* Post /:doctor_id/update_price		修改价格


参数说明：(同上)

返回值：


测试程序 

python update_doctor_main_desc.py  23 testtest

python update_doctor_price.py 23 88

python update_doctor_avatar.py 23 http://h.hiphotos.baidu.com/baike/w%3D790/sign=087bc013a6ec08fa260011ae69ef3d4d/2934349b033b5bb53692445230d3d539b700bcd1.jpg

python create_reply.py 96 22 hew


返回值：

* {result：200} 调用成功
* {result：400} 调用失败


## reply

创建路径：Post /reply

参数说明：

* id: 回复主键
* reply_desc: 回复内容
* basic_case_id: 对应咨询编号


返回值：
* {result：200}： 调用成功
* {result：400}： 调用失败 
* {result：200}： 调用成功
* {result：400}： 调用失败 


## reply

创建路径：Post /reply

参数说明：

* id: 回复主键
* reply_desc: 回复内容
* basic_case_id: 对应咨询编号


返回值：
* {result：200}： 调用成功
* {result：400}： 调用失败 



# 对外接口（读取操作）
## 读取某医生待咨询问题列表

###传入医生ID

###返回说明
```javascript
{
    "num": 10, #记录总数
    "data": [
        {
            "name": "xiaowei",#姓名
            "user_id":15 #用户id
            "basic_case_id":20, #咨询id
            "main_desc:"" #咨询主题
        },
        ...
    ]
}
```
---



## 读取某病人咨询信息

###传入咨询ID


###返回说明
```javascript
{
	"basic_case":
	{
	"main_desc":"xxx",#主诉
	"detail_desc":"XX",#详细描述
	"treat_desc":"" #诊疗经过
    "now_desc":"" #目前情况
    },
    "body_sign":{
     "temperature":38, #体温
     "pulse":120, #心跳
     "high_pressure":110, #高压
     "low_pressure":90, #低压
     "swelling":"xx", #肿胀
     "status_name":"" #其他体征
     },
     “sick_asset”:[
	     {
	     	"title":"xx",#附件标题
	     	"desc":"xx",#附件说明
	     	"asset":"xxxx",#附件url
	     	"asset_type":"xxxx",#附件类型

    	 },

     ...
     ]
    }

}
```
---


## 读取某病人病历信息

