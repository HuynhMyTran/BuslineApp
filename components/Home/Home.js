import { View, Text, TextInput, ActivityIndicator, Image, ScrollView } from "react-native"
import MyStyle from "../../styles/MyStyle"
import { useEffect, useState } from "react"
import Apis, { endpoints } from "../../Apis";
import moment from "moment";


const Home = () => {
    const[route, setRoute] = useState(null);
    useEffect(()=>{
        const loadRoute = async() => {
            const res = await fetch(Apis.get(endpoints['route']));
            setRoute(res.data.results)
        }
        loadRoute();
    },[]);

    return <View style={MyStyle.container}>
        <Text style={MyStyle.subject} >Dịch Vụ Đặt Vé Xe</Text>
        {route === null?<ActivityIndicator color={'gray'}/>:<ScrollView>
            {route.map(c=>(
                <View style={[MyStyle.row, {padding: 5}]} key={c.id}>
                    <View style={{flex: 1}}>
                        <Image style={{width:100, height:100}} source={{uri:c.image}} ></Image>
                    </View>
                    <View style={{flex: 2}}>
                        <Text style={MyStyle.title}>{c.name}</Text>
                        <Text style={{marginLeft: 5}}>{moment(c.created_date).fromNow()}</Text>
                    </View>
                </View>
            ))}
        </ScrollView>}
    </View>
}

export default Home