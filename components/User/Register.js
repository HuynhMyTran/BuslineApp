import { View, Text, TextInput, ActivityIndicator, Dimensions, Image } from "react-native"
import MyStyle from "../../styles/MyStyle"
import Styles from "./Styles";
import { TouchableOpacity } from "react-native-gesture-handler";
import { useContext, useState } from "react";
import MyContext from "../../MyContext";
import Apis, { authApi, endpoints } from "../../Apis"; 
import * as ImagePicker from 'expo-image-picker';

const{width} = Dimensions.get('window')

const Register = ({navigation}) => {
    const [user, setUser] = useState({
        'first_name': "",
        'last_name': "",
        'username': "",
        'password': "",
        'email':"",
        'avatar': ""
    });

    const [loading, setLoading] = useState();

    const register = () => {

    }

    const change = (field, value) => {
        setUser(current => {
            return {...current,[field]: value}
        })

    }

    const picker = async () => {
        const {status} = await ImagePicker.requestMediaLibraryPermissionsAsync();
        if (status!=="granted"){
            alert("Permission denied");
        } else {
            const res = await ImagePicker.launchImageLibraryAsync();
            if(!res.canceled){
                change('avatar', res.assets[0]);
            }
        }
    }

    return <View style={MyStyle.container}>
        <Text style={MyStyle.subject}>Đăng Ký</Text>
        <TextInput value={user.username} onChangeText={u=>change('username',u)} placeholder="Tên tài khoản..." style={Styles.input}></TextInput>
        <TextInput secureTextEntry={true} value={user.password} onChangeText={u=>change('password',u)} placeholder="Mật khẩu..." style={Styles.input}></TextInput>
        <TextInput secureTextEntry={true}  placeholder="Nhập lại mật khẩu..." style={Styles.input}></TextInput>
        <TextInput value={user.first_name} onChangeText={u=>change('first_name',u)} placeholder="Tên..." style={Styles.input}></TextInput>
        <TextInput value={user.last_name} onChangeText={u=>change('last_name',u)} placeholder="Họ và tên lót..." style={Styles.input}></TextInput>
        <TextInput value={user.email} onChangeText={u=>change('email',u)} placeholder="Email..." style={Styles.input}></TextInput>
        <TouchableOpacity onPress={picker}>
            <Text style={{...Styles.input, width: width}}>Chọn avatar...</Text>
        </TouchableOpacity>

        <Image source={{uri: user.avatar.url}} style={{width:100, height:100, margin: 0}}></Image>

        {loading===true?<ActivityIndicator />:<>
            <TouchableOpacity onPress={register}>
                <Text style={Styles.button}>Register</Text>
            </TouchableOpacity>
        </>
        }
    </View>
}

export default Register;