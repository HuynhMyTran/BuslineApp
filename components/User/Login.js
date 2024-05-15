import { View, Text, TextInput, ActivityIndicator } from "react-native"
import MyStyle from "../../styles/MyStyle"
import Styles from "./Styles";
import { TouchableOpacity } from "react-native-gesture-handler";
import { useContext, useState } from "react";
import MyContext from "../../MyContext";
import Apis, { authApi, endpoints } from "../../Apis";


const Login = ({navigation}) => {
    const [username, setUsername] = useState();
    const [password, setPassword] = useState();
    const [user,dispatch] = useContext(MyContext);
    const [loading, setLoading] = useState();

    const login = async () => {
        setLoading(true);
        try {
            let res = await Apis.post(endpoints['login'], {
            'client_id': 'ffRWhBnaCbzzUSydlzyvY2GwYsNAqZyRFCQi6pHj',
            'client_secret': 'OYqo4EAe9T6iyh9mD556Uf6xq8xNPLlssAkuBBQwe2XMnSXE1FOT3cNQyhf8HbQsg3nK79nLA2mXO48GQK7VN30QyyybFjNwENCfJkBsjPQzXrNrrbAM00OagjdpRxAR',
            'username': username,
            'password': password,
            'grant_type': 'password'
           })
           console.info(res.data)
           let user = await authApi(res.data.access_token).get(endpoints['users']);
           console.info(user.data)
           dispatch({
            'type': 'login',
            'payload': {
                'username': user.data.username
            }
        })
            navigation.navigate('Home');
        } catch (error) {
            console.error(error);
        } finally{
            setLoading(false);
        }
    }


    return <View style={MyStyle.container}>
        <Text style={MyStyle.subject}>Đăng Nhập</Text>
        <TextInput value={username} onChangeText={u=>setUsername(u)} placeholder="Tên tài khoản..." style={Styles.input}></TextInput>
        <TextInput secureTextEntry={true} value={password} onChangeText={p=>setPassword(p)} placeholder="Mật khẩu..." style={Styles.input}></TextInput>
        {loading===true?<ActivityIndicator />:<>
            <TouchableOpacity onPress={login}>
                <Text style={Styles.button}>Login</Text>
            </TouchableOpacity>
        </>
        }
    </View>
}

export default Login;