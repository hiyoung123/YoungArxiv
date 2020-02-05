/* eslint-disable react/jsx-no-undef */
import Taro, { Component }from '@tarojs/taro'
import { View } from '@tarojs/components'
import { AtList, AtListItem } from "taro-ui"

export default class PaperList extends Component {
    static defaultProps = {
        list: []
    }

    render () {
        return (
            <View>              
                <AtList>
                    {this.props.list.map(item => 
                        <AtListItem
                        title={item.title}
                        note={item.author}
                        arrow='right'
                        thumb='http://img12.360buyimg.com/jdphoto/s72x72_jfs/t10660/330/203667368/1672/801735d7/59c85643N31e68303.png'
                        />
                    )}
                </AtList> 
            </View>
        )
    }
}