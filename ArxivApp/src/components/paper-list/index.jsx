/* eslint-disable react/jsx-key */
/* eslint-disable react/require-render-return */
/* eslint-disable react/jsx-no-undef */
import Taro, { Component }from '@tarojs/taro'
import { View } from '@tarojs/components'
import './index.scss'

export default class PaperList extends Component {
    static defaultProps = {
        list: []
    }

    handleClick = (itemid) => {
        console.log('click item ', itemid)
    }

    render () {
        const { list } = this.props
        return (
            <View>
                { list.map((item) => {
                    return (
                        <View className='paper-item' onClick={this.handleClick.bind(this,item.id)}>              
                            <View className='paper-title'>
                                <Text>{ item.title }</Text>
                            </View>
                            <View className='paper-info'>
                                <Text className='line-1'>{ item.summary }</Text>
                            </View>
                            <View className='paper-author'>
                                <View>{ item.author }</View>
                            </View>
                        </View>
                    )
                })}
            </View>
        )
    }
}
