import { StyleSheet } from "react-native";

export default MyStyle = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "top",
        alignItems:"center",
        backgroundColor:"lightblue",
    },

    subject:{
        fontSize: 30,
        fontWeight: "bold",
        color: "black"
    },

    row:{
        flexDirection: "row"
    },

    title:{
        fontSize: 12,
        fontWeight: "bold",
        color: "black",
        marginLeft: 5
    }
})