import Taro, { Component } from '@tarojs/taro'
import { View, Text, Image } from '@tarojs/components'
import loading from './assets/loading.gif'
import './index.scss'

export default class Loading extends Component {
  render () {
    return (
      <View className='comp-loading'>
        <Image src={loading} className='comp-loading__img' />
        <View className='home__loading'><Text className='comp-loading__text'>正在加载中...</Text></View>
      </View>
    )
  }
}

