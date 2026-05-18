/* 
=============================================================================
   地级市方言矢量地图	
=============================================================================
*/		 


/* 
=======================================
   处理并合并各方言数据数据	
=======================================
*/


// 导入方言数据
import excel "多样性数据.xlsx",sheet("Sheet1") firstrow clear

// 重命名变量名称
rename (diversity1方言分化指数 diversity2方言片个数) ///
(div_index dialect_count)

// 保留所需变量
keep city div_index dialect_count

// 把方言数据与地图数据的城市名称对应
replace city = "定西市" if city == "定西地区"
replace city = "陇南市" if city == "陇南地区"
replace city = "平凉市" if city == "平凉地区"
replace city = "庆阳市" if city == "庆阳地区"
replace city = "张掖市" if city == "张掖地区"
replace city = "百色市" if city == "百色地区"
replace city = "河池市" if city == "河池地区"
replace city = "贺州市" if city == "贺州地区"
replace city = "毕节市" if city == "毕节地区"
replace city = "铜仁市" if city == "铜仁地区"
replace city = "普洱市" if city == "思茅地区"
replace city = "昭通市" if city == "昭通地区"
replace city = "固原市" if city == "固原地区"
replace city = "海东市" if city == "海东地区"
replace city = "商洛市" if city == "商洛地区"
replace city = "丽江市" if city == "丽江地区"
replace city = "哈密市" if city == "哈密地区"
replace city = "临沧市" if city == "临沧地区"
replace city = "三门峡市" if city == "三门峽市"
replace city = "吐鲁番市" if city == "吐鲁番地区"

// 方言数据中巢湖市和莱芜市两个市以撤市并入合肥市和济南市
replace dialect_count = dialect_count + 1 ///
if city == "合肥市" | city == "济南市"

drop if city == "莱芜市" | city == "巢湖市"

// 重新排列数据
gsort city

// 保存数据
save "方言绘图数据.dta", replace

// 把方言数据和地图数据进行合并
merge 1:1 city using "china_city_db.dta"
drop _merge

// 把没有方言的城市的方言数量设置为1，其他城市在原来的数量上加1
replace dialect_count = dialect_count + 1 if !missing(dialect_count)
replace dialect_count = 1 if missing(dialect_count)

// 删去异常的数据
drop if city == "中朝共有"

// 重新排列数据
gsort province city

// 保存数据
save "方言与城市合并数据.dta", replace


/* 
=======================================
   绘制地级市方言矢量地图	
=======================================
*/


// 调用合并数据作图
use "方言与城市合并数据.dta", clear

gen div_index_2d = round(div_index, 0.01)

// 使用spmap命令绘制中国地级市方言矢量地图
spmap div_index_2d using "china_city_coord.dta", id(ID) ///
fcolor(Blues2) clmethod(quantile) ///
legend(position(8)) legtitle("方言分化指数") legstyle(1) ///
graphr(margin(medium)) ///
legend(size(*1.2)) ///
line(data(china_city_line_coord.dta) size(*0.5 ...) color(black) select(keep if _ID <= 6)) ///
label(data(china_city_label) x(x_centroid) y(y_centroid) l(label) color(black) size(*0.8)) ///
xsize(12) ysize(10) ///

// 导出为PNG格式
graph export "中国地级市方言数量分布地图.png", replace

// 调用合并数据作图
use "方言与城市合并数据.dta", clear

gen div_index_2d = round(div_index, 0.01)

// 使用spmap命令绘制中国地级市方言矢量地图
spmap div_index_2d using "china_city_coord.dta", id(ID) ///
fcolor(Reds2) clmethod(quantile) ///
legend(position(8)) legtitle("方言分化指数") legstyle(1) ///
graphr(margin(medium)) ///
legend(size(*1.2)) ///
line(data(china_city_line_coord.dta) size(*0.5 ...) color(black) select(keep if _ID <= 6)) ///
label(data(china_city_label) x(x_centroid) y(y_centroid) l(label) color(black) size(*0.8)) ///
xsize(12) ysize(10) ///

// 导出为PNG格式
graph export "中国地级市方言数量分布地图（红色版）.png", replace