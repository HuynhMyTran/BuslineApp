import { createDrawerNavigator } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Home from './components/Home/Home';
import Login from './components/Login/Login';

const Drawer = createDrawerNavigator();

export default App = () => {
  return <NavigationContainer>
      <Drawer.Navigator>
          <Drawer.Screen name='Home' component={Home}></Drawer.Screen>
          <Drawer.Screen name='Login' component={Login} />
      </Drawer.Navigator>
  </NavigationContainer>
}