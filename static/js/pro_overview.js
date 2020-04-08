
window.onload = function() {
    var firstFlag = true;
    

    function convertData(data) {
        var res = [];
        for (var i = 0; i < data.length; i++) {
            var geoCoord = styleArr[data[i].name];
            if (geoCoord) {
                res.push({
                    name: data[i].name,
                    value: geoCoord.concat(data[i].value)
                });
            }
        }
        return res;
    };
    
    var locArr = {};
    var styleArr = [];
    var myRadar;
    var myChart;
    var healthyChart;
    var cement_num = 0;
    var wind_num = 0;
    var water_num = 0;

    function removeElement(_element) {
        var _parentElement = _element.parentNode;
        if (_parentElement) {
            _parentElement.removeChild(_element);
        }
    }

    var option = {
        tooltip: {
            trigger: 'item',
            formatter: function (params)//数据格式
            {
                var relVal = "";
                if (params.value != "-") {
                    relVal += "风场名称: " + params.value[2].facName + "<br/>";
                    relVal += "工作人员: " + params.value[2].name + "<br/>";
                }
                return relVal;
            },
            position: function (pos) {
                return [pos[0], pos[1] + 5];
            },
        },
        geo: {
            map: 'china',
            nameMap:{},
            roam: true,
            zoom: 1.2,
            selectedMode:'single',
            label: {
                normal: {
                    show: true,
                    textStyle: {
                        color: 'rgba(0,244,253,0.7)',
                        fontSize: 10
                    }
                }
            },
            itemStyle: {
                normal:{
                    areaColor:'#1492f0',
                    borderColor: 'rgba(0,244,253,0.7)',
                },
                emphasis:{
                    label: {
                        textStyle: {
                            color: 'rgba(0,244,253,0.7)'
                        },
                        show: true
                    },
                    areaColor: 'rgba(0,244,253,0.7)',
                    shadowOffsetX: 0,
                    shadowOffsetY: 0,
                    borderWidth: 0,
                    borderColor: '#002249'
                }
            },
            scaleLimit:{
                max:4
            }
        },
        series : [
            {
                type: 'scatter',
                coordinateSystem: 'geo',
                name:'china',
                data: [],
                symbolSize: 15,
                symbolRotate:15,
                symbol: 'pin',
                label: {
                    normal: {
                        formatter: '{b}',
                        position: 'right',
                        show: false
                    },
                    emphasis: {
                        show: true
                    }
                },
                emphasis:{
                    itemStyle:{
                        borderColor:"#fff",
                        borderWidth:2
                    }
                }
            }]
    };

    

    initMap();
    setInterval(initMap, 120000);
    function initMap() {
        let result = [
            {
                id:123456,
                facName:"茶山",
                name:"小二",
                address:"11",
                x:"120.58",
                y:"30.01",
                status:"1"
            },
            {
                id:987654,
                facName:"寒风凌",
                name:"网小二",
                address:"19",
                x:"114.07",
                y:"22.62",
                status:"2"
            }
        ]
        /*$.ajax({
            type: "POST",
            url: getApi(2,false,"overview/whole"),
            // url: "../../overview/whole",
            data: {},
            xhrFields: {
                withCredentials: true
            },
            dataType: "json",
            error: function() {},
            success: function(result) {*/
        if (null != result && result.length > 0) {
            parent.fields_arr = result;
            locArr = [];
            styleArr = [];

            var provinceArr = {};
            // provinceArr["name"] = "123456";
            var dataArr = {};
            var nameObj = {};
            var valueObj = {};
            var itemStyleObj = {};
            function buildProvince(obj) {
                if (provinces[obj.address] != null) {
                    var province = provinces[obj.address];
                    if (provinceArr[province] == null) {
                        provinceArr[province] = {};
                        provinceArr[province][obj.name] = [obj.loc_x, obj.loc_y];
                        provinceArr[province].mac_num = obj.allnum;
                    } else {
                        provinceArr[province][obj.name] = [obj.loc_x, obj.loc_y];
                        provinceArr[province].mac_num += obj.allnum
                    }
                }
            }
            function buildData(obj) {
                if (provinces[obj.address] != null) {
                    var province = provinces[obj.address];
                    if (dataArr[province] == null) {
                        dataArr[province] = [];
                        // dataArr[province].push(obj);
                        dataArr[province] = dataArr[province].concat([{"name":obj.name,"facName":obj.facName,"value":[obj.loc_x, obj.loc_y,obj],"itemStyle":obj.itemStyle}]);
                    } else {
                        // dataArr[province].push(obj);
                        dataArr[province] = dataArr[province].concat([{"name":obj.name,"facName":obj.facName,"value":[obj.loc_x, obj.loc_y,obj],"itemStyle":obj.itemStyle}]);
                    }
                }
            }

            for (var i = 0; i < result.length; i++) {
                var obj = {};
                obj.facName = result[i]["facName"];
                obj.name = result[i]["name"];
                obj.address = result[i]["address"];
                obj.loc_x = result[i]["x"];
                obj.loc_y = result[i]["y"];
                if (result[i]["status"] == 3) {
                    obj.itemStyle = {
                        color: "#f80000"
                    };
                    obj.status = 3; //报警状态
                } else if (result[i]["status"]== 2) {
                    obj.itemStyle = {
                        color: "#ffa101"
                    };
                    obj.status = 2;
                } else if (result[i]["status"] ==1) {
                    obj.itemStyle = {
                        color: "#009944"
                    };
                    obj.status = 1;
                }
                obj.id = result[i].id;

                styleArr.push(obj);
                locArr = locArr.concat([{"name":result[i]["name"],"value":[result[i]["x"], result[i]["y"],obj],"itemStyle":obj.itemStyle}]);
                buildProvince(obj);
                buildData(obj);
            }

            if (myChart != null && myChart != "" && myChart != undefined) {
                myChart.dispose();
            }
            myChart = echarts.init(document.getElementById("map_china"));
            option.series[0].data = locArr;

            myChart.setOption(option);

        } else {
            swal("无现场数据");
        }
    }
    // });
}



    var provinces = {
        "1": "北京",
        "2": "天津",
        "9": "上海",
        "22": "重庆",
        "3": "河北",
        "4": "山西",
        "6": "辽宁",
        "7": "吉林",
        "8": "黑龙江",
        "10": "江苏",
        "11": "浙江",
        "13": "福建",
        "12": "安徽",
        "14": "江西",
        "15": "山东",
        "16": "河南",
        "17": "湖北",
        "18": "湖南",
        "19": "广东",
        "21": "海南",
        "23": "四川",
        "24": "贵州",
        "25": "云南",
        "27": "陕西",
        "28": "甘肃",
        "29": "青海",
        "34": "台湾",
        "5": "内蒙古",
        "20": "广西",
        "26": "西藏",
        "30": "宁夏",
        "31": "新疆",
        "32": "香港",
        "33": "澳门",
        "10001": "国外"
    };
    function cloneObj(obj) {
        var newObj = {};
        if (obj instanceof Array) {
            newObj = [];
        }
        for (var key in obj) {
            var val = obj[key];
            newObj[key] = typeof val === "object" ? cloneObj(val) : val;
        }
    }

$(window).resize(function() {
    window.location.reload();
});
