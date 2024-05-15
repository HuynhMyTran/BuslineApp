import { View, Text, TextInput, ActivityIndicator, Image, ScrollView } from "react-native"
import MyStyle from "../../styles/MyStyle"
import { useEffect, useState } from "react"
import Apis, { endpoints } from "../../Apis";
import moment from "moment";


const Home = ({route}) => {
    // const[buses, setBuses] = useState(null);
    // const {cateId} = route.params?.cateId;

    // useEffect(()=>{
    //     let url = endpoints['buses'];
    //     if (cateId !== null && cateId !== "" ){
    //         url = `${url}?category_id=${cateId}`;
    //     }
    //     const loadBuses = async() => {
    //         const res = await Apis.get(url);
    //         setBuses(res.data.results)
    //     }
    //     loadBuses();
    // },[cateId]);

    // return <View style={MyStyle.container}>
    //     <Text style={MyStyle.subject} >Dịch Vụ Đặt Vé Xe</Text>
    //     {buses === null?<ActivityIndicator color={'gray'}/>:<ScrollView>
    //         {buses.map(b=>(
    //             <View style={[MyStyle.row, {padding: 5}]} key={b.id}>
    //                 <View style={{flex: 1}}>
    //                     <Image style={{width:100, height:100}} source={{uri:c.image}} ></Image>
    //                 </View>
    //                 <View style={{flex: 2}}>
    //                     <Text style={MyStyle.title}>{b.name}</Text>
    //                     <Text style={{marginLeft: 5}}>{moment(c.created_date).fromNow()}</Text>
    //                 </View>
    //             </View>
    //         ))}
    //     </ScrollView>}
    // </View>
}

export default Home