# Database description

## Client table:
1. client_id (客户id)
2. openid (客户微信id)
3. name (客户姓名)
4. enmergency_contact（紧急联系人）
5. contact （联系方式）
6. contact2
7. contact3
8. address （地址）
9. company_name （公司名称）

## plant_info
1. plant_id （厂房id）
2. rent_rate （租金上涨率）
3. property_rate （物业上涨率）
4. rent （租金）
5. property （物业）
6. area （面积）
7. owner （厂房所有人）

## contract_info
1. contract_id （合同ID）
2. client_id （客户ID）
3. plant_id （厂房ID）
4. area （面积）
5. plant_address （厂房地址）
6. start_date （开始日期）
7. end_date （结束日期）
8. type_payment （付款方式）
9. rent_fee （租金）
10. deposit （押金）
11. property_fee （物业费）
12. rent_rate （租金上涨率）
13. property_fee (can be none)（物业上涨率）
14.  water_unit_fee (can be none) （水费单价）
15.  tax (can be none) （税点）
16.  overdue_fee （滞纳金）
17.  penal_fee （违约金）
18.  agency_name （中介名称）
19.  agency_fee （中介费）
20.  agency_fee_paid （已付中介费）
21.  agency_fee_unpaid （未付）
<!-- 22.  power_id(FK) -->
22. type （用电类型）
23. unit_fee （单价， 三个用电类型）
24. power_high_fee （高峰电费）
25. power_low_fee （低谷电费）
26. power_normal_fee （平均电费）
27. kv_bought （每月购买kv数）
28. coeffient （消耗系数）
29. ammeter_mul （电表倍数）
30. renew （合同续约）
<!-- ## power_type_info
1. power_id
2. contract_id
3. type
4. unit_fee
5. power_high_fee
6. power_low_fee
7. power_normal_fee
8. kv_bought
9. coeffient
10. ammeter_mul -->
## bill_power
1. bill_power_id （电费账单ID）
2. contract_id （合同ID）
3. date_paid （已交日期）
4. type （用电类型）
5. unit_fee （单价）
6. kv_fee （kv 总价）
7. power_high （高峰用电度数）
8. power_low （低谷用电度数）
9. power_normal （均值用电读书）
10. total （电费总额）
11. state （状态）
12. operator （操作人员）
13. paid_fee （已交费用）

## bill_water
1. bill_water_id （水费账单ID）
2. contract_id （合同ID）
3. date_paid （已交日期）
4. state （状态）
5. degree_water_meter （水表抄数）
6. ton （用水吨数）
7. total （水费总额）
8. paid_fee （已交费用）

## bill_rent
1. bill_rent_id （租金账单ID）
2. contract_id （合同ID）
3. date_paid （已日期）
4. paid_fee （已交费用）
5. state （状态）
6. operator （操作人员）

## bill_property
1. bill_property_id （物业账单ID）
2. contract_id （合同ID） 
3. date_paid （已交日期）
4. paid_fee （已交费用）
5. state （状态）
6. operator （操作人员）
7. total （物业总额）

## notice
1. notice_id（通知ID）
2. title （标题）
3. content（内容）
4. type（类型）
5. client_openid （用户openid）
6. date （日期）
7. publisher （发布人）

## repair
1. repair_id （维修ID）
2. user_id （维修人员）
3. state （状态）
4. username （发起人姓名）
5. charger （负责人）
6. description （描述）

## user 
1. user_id （用户id）
2. username （用户名）
3. password （密码）
4. role_id （角色）
5. user_name (用户名字)

## role
1. role_id （角色ID）
2. name （角色名称）
3. permission （角色权限）
