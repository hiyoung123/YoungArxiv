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
                        <View className='feed-item'>              
                            <View className='question' onClick={this.navigateTo.bind(this,'/pages/question/question')}>
                                <Text>{ item.title }</Text>
                            </View>
                            <View className='answer-body'>
                                <View>
                                    <Text className='answer-txt' onClick={this.navigateTo.bind(this,'/pages/answer/answer')} >{ item.summary }</Text>
                                </View>
                                <View className='answer-actions'>
                                    <View className='like dot'>
                                        <View>{ item.author } </View>
                                    </View>
                                </View>
                            </View>
                        </View>
                    )
                })}
            </View>
        )
    }
}
                            {/* <AtListItem
                                title={item.title}
                                note={item.author}
                                arrow='right'
                                thumb='http://img12.360buyimg.com/jdphoto/s72x72_jfs/t10660/330/203667368/1672/801735d7/59c85643N31e68303.png'
                            /> */}