/* eslint-disable react/jsx-closing-bracket-location */
/* eslint-disable no-unused-vars */
/* eslint-disable react/jsx-indent-props */
/* eslint-disable react/no-unused-state */
import Taro, { Component }from '@tarojs/taro'
import { View, Text } from '@tarojs/components'
import { AtTabBar } from "taro-ui"
import { connect } from '@tarojs/redux'
import Loading from "../../components/loading";
import FakeSearchBar from "../../components/fake-search-bar";
import PaperList from "../../components/paper-list";
import URL from "../../constants/urls";
import { 
    getNewPapers,
    getHotPapers,
    getRecommendPapers
 } from "../../actions/home"

 import './index.scss'

@connect(
    ({ home }) => ({
        papers : home.papers
    //   newPapers: home.newPapers,
    //   hotPapers: home.hotPapers,
    //   recommendPapers: home.recommendPapers
    }),
    {
      dispatchGetNewPapers: getNewPapers,
      dispatchGetHotPapers: getHotPapers,
      dispatchGetRecommendPapers: getRecommendPapers,
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
        loaded: false,
        loading: false,
      }

    componentDidMount() {
        this.fetchData(this.state.current)
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
        })
        this.fetchData(value)
    }

    fetchData(type) {
        this.setState({ loading: true, loaded: false })
        console.log(type)
        switch(type){
            case 0:
                this.props.dispatchGetNewPapers().then((res) => {
                    this.setState({ loading: false, loaded: true })
                });
                break
            case 1:
                this.props.dispatchGetHotPapers().then((res) => {
                    this.setState({ loading: false, loaded: true })
                });
                break
            case 2:
                this.props.dispatchGetRecommendPapers().then((res) => {
                    this.setState({ loading: false, loaded: true })
                });
                break
        } 
    }

    render () {
        return (
            <View>  
                <FakeSearchBar onClick={this.onClickSearchBar} />
                {/* <View>广告栏</View> */}
                <AtTabBar 
                    tabList={[
                        { title: '最新' },
                        { title: '热门' },
                        { title: '推荐' }
                        ]}
                    onClick={this.handleClick}
                    current={this.state.current}
                />
    { this.state.loaded === true && <PaperList list={this.props.papers} /> }
    { this.state.loaded === false && <Loading /> }
    {this.state.loading && <View className='home__loading'>
              <Text className='home__loading-txt'>正在加载中...</Text>
            </View>
          }
            </View>
        )
    }
}

export default Home