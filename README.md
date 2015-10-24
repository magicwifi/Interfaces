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
 
### 创建路径: Post /doctors

参数说明 

* doctor_id: 医生主键
* name：医生姓名
* avatar：头像路径
* main_desc: 简要说明
* url: 主页地址
* price: 单价

测试程序 python create_doctor.py  23  Jack

返回值：

* {result：200} 调用成功
* {result：400} 调用失败


### 更新路径：

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

创建路径：Post /:basic_case_id/:doctor_id/create_reply

参数说明：

* doctor_id: 医生编号
* main_desc: 回复内容
* basic_case_id: 对应咨询编号
* sick_name: 疾病名称

测试程序：

python create_reply.py 97 23 hello


返回值：
* {result：200}： 调用成功
* {result：400}： 调用失败 



# 对外接口（读取操作）
## 读取某医生待咨询问题列表

###传入医生ID

样例路径

http://117.34.78.201:8081/10/index_basic_cases.json



###返回说明
```javascript
{	
     	code:"200", #调用成功
	"result": [
	{"basic_case_id":45, #咨询编号
	"basic_case_title":"tewet", #咨询主题
	"user_id":27,	#待诊病人编号
	"user_name":"not open",	#待诊病人姓名
	"user_age":"not open",	#待诊病人年龄
	"user_gender":"not open"},	#待诊病人性别
        ...
    ]
}
```
---



## 读取某病人咨询信息

###传入咨询ID

样例路径

http://117.34.78.201:8081/92/show_basic_case.json


###返回说明
```javascript
{	"code" #调用成功,
	"basic_case":{"id":92,
	"main_desc":"hi", #主诉
	"detail_desc":"heqwe",	#详细描述
	"treat_desc":"",	#诊疗经过
	"now_desc":"normal",	#目前情况
	"created_at":"2015-10-21T20:30:38.000+08:00",	#创建时间
	"updated_at":"2015-10-22T19:38:05.000+08:00",	#更新时间
	"poster":null,
	"user_id":32,	#咨询用户主键
	"public":true,	#用户是否公开病历
	"doctor_id":1,	#咨询医生主键
	"process":"fee"},
	"body_sign":{"id":77,	
	"temperature":0,	#体温
	"pulse":0,		#脉搏每分钟
	"high_pressure":30,	#高压
	"low_pressure":60,	#低压
	"swelling":"littleswelling",	#双下肢是否肿胀
	"basic_case_id":92,		
	"created_at":"2015-10-21T20:30:38.000+08:00",
	"updated_at":"2015-10-22T19:36:57.000+08:00"
	,"status_name":"xiongmen yanqianfahei "},	#其他体征
	"sick_assets":[{"id":20,"
	title":"hllo",	#附件名称
	"desc":"eqw",	#附件描述
	"created_at":"2015-10-22T19:37:40.000+08:00",
	"updated_at":"2015-10-22T19:37:47.000+08:00",
	"poster":null,
	"asset":"Fggf_Cnom43OEGZVB7wFS7id3SsP",	#附件路径
	"basic_case_id":92,
	"size":785915,
	"filename":"chan.jpg",
	"content_type":"image/jpeg",
	"position":1,
	"asset_type":"CT"	#附件类型
	}]	


	
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

