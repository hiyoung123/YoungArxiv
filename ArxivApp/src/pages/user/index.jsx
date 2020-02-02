import Taro, { Component }from '@tarojs/taro'
import { View } from '@tarojs/components'

export default class User extends Component {

    config = {
        navigationBarTitleText : "个人中心"
    }
    render () {
        return (
            <View> user </View>
        )
    }
}