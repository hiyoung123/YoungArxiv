/* eslint-disable react/jsx-indent-props */
/* eslint-disable react/no-unused-state */
import Taro, { Component }from '@tarojs/taro'
import { View } from '@tarojs/components'
import { AtTabBar } from 'taro-ui'
import { connect } from '@tarojs/redux'
import FakeSearchBar from "../../components/fake-search-bar";
import URL from "../../constants/urls";
import { getNewPapers } from "../../actions/home"

@connect(
    ({ home }) => ({
      newPapers: home.newPapers,
    }),
    {
      dispatchGetNewPapers: getNewPapers,
    }
  )

class Home extends Component {

    constructor() {
        super(...arguments);
        this.onClickSearchBar = this.onClickSearchBar.bind(this);
        this.handleClick = this.handleClick.bind(this);
    }

    state = {
        current : 0,
      }

    componentDidMount() {
        this.props.dispatchGetNewPapers()
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
                <View> {this.props.newPapers[0].title} </View>
            </View>
        )
    }
}

export default Home