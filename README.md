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
* avatar：头像路径(可为空)
* main_desc: 简要说明
* url: 主页地址
* hospital: 医院
* room:	科室
* rank: 职称
* level: 华仁医生级别
* sex: 性别
* speciality: 擅长

Reservation 预约

* support_number: 预约人数
* price: 单价
* type: 类型
* remark: 备注 （可为空）


测试程序 python create_doctor.py  23  Jack

返回值：

* {result：200} 调用成功
* {result：400} 调用失败


### 更新路径：

* Post /:doctor_id/update_doctor_avatar	修改头像
* Post /:doctor_id/update_doctor_url	修改主页
* Post /:doctor_id/update_main_desc	修改说明


参数说明：(同上)

返回值：


测试程序 

python update_doctor_main_desc.py  23 testtest


python update_doctor_avatar.py 23 http://h.hiphotos.baidu.com/baike/w%3D790/sign=087bc013a6ec08fa260011ae69ef3d4d/2934349b033b5bb53692445230d3d539b700bcd1.jpg


* Post /:doctor_id//update_doctor_reservation
* 修改某类预约的价格
* 修改某类预约的预约人数


python update_doctor_reservation.py 23 fee 88


## reply


创建路径：Post /:basic_case_id/:doctor_id/create_reply

参数说明：

* doctor_id: 医生编号
* main_desc: 回复内容
* basic_case_id: 对应咨询编号
* sick_name: 一级疾病名称
* sick_name_sub: 二级疾病名称

测试程序：
python create_reply.py 105 23 hew hello

返回值：

* {result：200} 调用成功
* {result：400} 调用失败



# 更新接口（加号）

更新路径：Post /:basic_case_id/update_plus

* basic_case_id: 对应咨询编号
* allow_plus: 是否加号


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
	"user_gender":"not open"
	"have_ct": true #是否有影像
	"process": 'fee' #咨询类型
	},	#待诊病人性别
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
	"basic_case":{"id":92,	#基本信息
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
	"body_sign":{"id":77,	#体征信息
	"temperature":0,	#体温
	"pulse":0,		#脉搏每分钟
	"high_pressure":30,	#高压
	"low_pressure":60,	#低压
	"swelling":"littleswelling",	#双下肢是否肿胀
	"basic_case_id":92,		
	"created_at":"2015-10-21T20:30:38.000+08:00",
	"updated_at":"2015-10-22T19:36:57.000+08:00"
	,"status_name":"xiongmen yanqianfahei "},	#其他体征
	"sick_assets":[{"id":20,"	#附件信息
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

    }

}
```
---


## 读取某病人病历信息

###传入病人ID

样例路径

http://117.34.78.201:8081/32/92/show_basic_info.json



###返回说明
```javascript
{	
     	code:"200", #调用成功
	"basic_info":{"id":28, 
	"name":"李明达",	#病人姓名
	"height":175.0,		#病人身高
	"weight":64.0,		#病人体重
	"gender":"male",	#病人性别
	"edited":true,		
	"user_id":32,		
	"created_at":"2015-10-21T20:30:38.000+08:00",
	"updated_at":"2015-10-22T19:50:02.000+08:00",
	"age":35,		#病人年龄
	"smokeinfo":"sometimes",	#病人是否抽烟
	"drink":"never",		#病人是否喝酒
	"smoke_account":5},		#每天吸烟多少根
	"hyperlipidemia":{"id":15,	#高脂血		
	"ishave":false,			#是否确诊
	"diagnosis_date":"2001-02-03T08:00:00.000+08:00",	#确诊日期
	"user_id":32,	
	"created_at":"2015-10-21T20:30:38.000+08:00",
	"updated_at":"2015-10-21T20:30:38.000+08:00"},
	"diabetes":{"id":17,	#糖尿病
	"ishave":true,	#是否确诊
	"limosis":60,	#餐前血糖
	"after_meal":120, #餐后血糖	
	"diagnosis_date":"2001-02-03T00:00:00.000+08:00",	#确诊日期
	"user_id":32,
	"created_at":"2015-10-21T20:30:38.000+08:00",
	"updated_at":"2015-10-22T19:34:42.000+08:00"},
	"hypertension":{"id":19,	#高血压
	"ishave":true,		#是否确诊
	"before_high":120,	#最高高压
	"before_low":60,	#最高低压
	"now_high":120,		#当前高压
	"now_low":60,		#当前低压
	"diagnosis_date":"2001-02-03T00:00:00.000+08:00",	#患病日期
	"user_id":32,
	"created_at":"2015-10-21T20:30:38.000+08:00",
	"updated_at":"2015-10-22T19:34:35.000+08:00"},
	"operation":[{"id":5,	#重大手术及外伤
	"title":"eqwe",		#手术名称
	"desc":"eee",		#详细说明
	"created_at":"2015-10-22T19:35:27.000+08:00",
	"updated_at":"2015-10-22T19:35:34.000+08:00",
	"poster":null,"public":null,	
	"price":null,
	"asset":"FuP0n2bDalakqHmm4rI3Pgg18k5n",	#手术附件路径	
	"user_id":32,
	"size":64135,
	"filename":"xulie1.jpg",
	"content_type":"image/jpeg",
	"position":1,
	"sick_date":"2015-10-23T00:00:00.000+08:00"}],	#手术日期
	"sicknesses":[{"id":24,	#病历附件路径
	"title":"heelo",	#病历名称
	"desc":"min",	#病历描述
	"created_at":"2015-10-22T19:35:46.000+08:00",
	"updated_at":"2015-10-22T19:35:55.000+08:00",
	"poster":null,
	"public":null,
	"price":null,
	"asset":"Fob0C1KawzlWP6-7UV-sleO9-Rn2",	#病历附件路径
	"user_id":32,"size":53224,
	"filename":"android1.jpg",	#病历名称
	"content_type":"image/jpeg",
	"position":1,
	"sick_date":"2015-10-23T00:00:00.000+08:00"},
	...
	]
}
```
---


###
其他说明

七牛云存储根目录：

http://7xmw39.com1.z0.glb.clouddn.com/


医生主页咨询路径:  

提交咨询 Post /check_my_doctor 

参数 doctor 医生姓名

commit	标示为commit时为提交咨询  标示为new时为新的咨询









