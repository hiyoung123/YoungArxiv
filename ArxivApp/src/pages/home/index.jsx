/* eslint-disable react/jsx-indent-props */
/* eslint-disable react/no-unused-state */
import Taro, { Component }from '@tarojs/taro'
import { View } from '@tarojs/components'
import { AtTabBar } from 'taro-ui'
import FakeSearchBar from "../../components/fake-search-bar";
import URL from "../../constants/urls";

export default class Home extends Component {

    constructor() {
        super(...arguments);
        this.onClickSearchBar = this.onClickSearchBar.bind(this);
        this.handleClick = this.handleClick.bind(this);
    }

    state = {
        current : 0,
        curList : [],
      }

    config = {
        navigationBarTitleText: "首页"
    };

    onClickSearchBar() {
        Taro.navigateTo({ url: URL.SEARCH });
    }

    handleClick(value) {
        this.setState({
            current: value,
            curList: ""
        })
    }

    render () {
        return (
            <View>  
                <FakeSearchBar onClick={this.onClickSearchBar} />
                <View>广告栏</View>
                <AtTabBar 
                    tabList={[
                        { title: '最新' },
                        { title: '热门' },
                        { title: '推荐' }
                        ]}
                    onClick={this.handleClick}
                    current={this.state.current}
                />
                <View>{ this.state.curList }</View>
            </View>
        )
    }
}
