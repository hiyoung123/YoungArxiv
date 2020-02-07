/* eslint-disable react/jsx-key */
/* eslint-disable react/require-render-return */
/* eslint-disable react/jsx-no-undef */
import Taro, { Component }from '@tarojs/taro'
import { View } from '@tarojs/components'
import { AtList, AtListItem } from "taro-ui"
import './index.scss'

export default class PaperList extends Component {
    static defaultProps = {
        list: []
    }

    render () {
        const { list } = this.props
        return (
            <View>
                { list.map((item) => {
                    return (
                        <View className='paper-item'>              
                            <View className='paper-title' onClick={this.navigateTo.bind(this,'/pages/question/question')}>
                                <Text>{ item.title }</Text>
                            </View>
                            <View className='paper-info'>
                                <Text className='line-1' onClick={this.navigateTo.bind(this,'/pages/answer/answer')} >{ item.summary }</Text>
                            </View>
                            <View className='paper-author'>
                                <View>{ item.author } </View>
                            </View>
                        </View>
                    )
                })}
            </View>
        )
    }
}
