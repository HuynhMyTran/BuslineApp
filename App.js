import { DrawerContent, DrawerContentScrollView, DrawerItem, DrawerItemList, createDrawerNavigator } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import { StatusBar } from 'expo-status-bar';
import React, { useEffect, useReducer, useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Home from './components/Home/Home';
import Apis, { endpoints } from './Apis';
import MyContext from './MyContext';
import MyUserReducer from './MyUserReducer';
import Login from './components/User/Login';
import Logout from './components/User/Logout';
import Register from './components/User/Register';



const Drawer = createDrawerNavigator();

export default App = () => {

  const [user, dispatch] = useReducer(MyUserReducer, null);

  return <MyContext.Provider value={[user, dispatch]}>
    <NavigationContainer>
      <Drawer.Navigator drawerContent={MyDrawerContent} screenOptions={{headerRight: Logout}}>
          <Drawer.Screen name='Trang Chủ' component={Home} options={{title: "Trang Chủ", hearderStyle:{backgoundColor:"black"}}}></Drawer.Screen>
          {user===null?<>
            <Drawer.Screen name='Đăng Nhập' component={Login} options={{title: "Đăng Nhập"}} />
            <Drawer.Screen name='Đăng Ký' component={Register} options={{title: "Đăng Ký"}} />
          </>:<>
            <Drawer.Screen name={user.username} component={Home} /> 
          </>}
      </Drawer.Navigator>
    </NavigationContainer>
  </MyContext.Provider>
}

const MyDrawerContent = (props) => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const loadCategories = async () => {
      const res = await Apis.get(endpoints['categories']);
      setCategories(res.data)
    }
    loadCategories();
  },[])

  return <DrawerContentScrollView {...props}>
    <DrawerItemList {...props} />
      {categories.map(c => <DrawerItem label={c.name} key={c.id} onPress={() => props.navigation.navigate("Home", {cateId: c.id})} ></DrawerItem>)}

  </DrawerContentScrollView>
}