/* eslint-disable react/jsx-closing-bracket-location */
/* eslint-disable no-unused-vars */
/* eslint-disable react/jsx-indent-props */
/* eslint-disable react/no-unused-state */
import Taro, { Component }from '@tarojs/taro'
import { View, ScrollView } from '@tarojs/components'
import { AtTabBar } from "taro-ui"
import { connect } from '@tarojs/redux'
import Loading from "../../components/loading";
import FakeSearchBar from "../../components/fake-search-bar";
import PaperList from "../../components/paper-list";
import URL from "../../constants/urls";
import { getWindowHeight } from '../../utils/style'
import { 
    getNewPapers,
    getHotPapers,
    getRecommendPapers
 } from "../../actions/home"

import './index.scss'

const RECOMMEND_SIZE = 10

@connect(
    ({ home }) => ({
        // papers : home.papers
    //   newPapers: home.newPapers,
    //   hotPapers: home.hotPapers,
    //   recommendPapers: home.recommendPapers
      home
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
        list : [],
        curIndex : 0,
        haveMore : true,
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
            haveMore: true
        })
        this.fetchData(value)
    }

    fetchData(type) {
        this.setState({ loading: true, loaded: false })
        console.log(type)
        switch(type){
            case 0:
                this.props.dispatchGetNewPapers().then((res) => {
                    this.setState({ loading: false, loaded: true, list: this.props.home.newPapers, curIndex: RECOMMEND_SIZE })
                });
                break
            case 1:
                this.props.dispatchGetHotPapers().then((res) => {
                    this.setState({ loading: false, loaded: true, list: this.props.home.hotPapers, curIndex: RECOMMEND_SIZE })
                });
                break
            case 2:
                this.props.dispatchGetRecommendPapers().then((res) => {
                    this.setState({ loading: false, loaded: true, list: this.props.home.recommendPapers, curIndex: RECOMMEND_SIZE })
                });
                break
        } 
    }

    fetchNextData(type) {
        if (!this.state.haveMore) {
            console.log('len :' + this.state.list.length)
            return
        }
        const lastedIndex = this.state.curIndex
        const paylod = {
            start : lastedIndex,
            size : RECOMMEND_SIZE
        }
        switch(type){
            case 0:
                this.props.dispatchGetNewPapers(paylod).then((res) => {
                    const newList = this.props.home.newPapers
                    const haveMore = newList.length === 0 ? false : true
                    this.setState({ 
                        loading: false, 
                        loaded: true,
                        haveMore : haveMore,
                        curIndex : lastedIndex + newList.length,
                        list: this.state.list.concat(newList) })
                });
                break
            case 1:
                this.props.dispatchGetHotPapers(paylod).then((res) => {
                    const newList = this.props.home.hotPapers
                    const haveMore = newList.length === 0 ? false : true 
                    this.setState({ 
                        loading: false,
                        loaded: true, 
                        haveMore : haveMore,
                        curIndex : lastedIndex + newList.length,
                        list: this.state.list.concat(newList) })
                });
                break
            case 2:
                this.props.dispatchGetRecommendPapers(paylod).then((res) => {
                    const newList = this.props.home.recommendPapers
                    const haveMore = newList.length === 0 ? false : true 
                    this.setState({ 
                        loading: false, 
                        loaded: true, 
                        haveMore : haveMore,
                        curIndex : lastedIndex + newList.length,
                        list: this.state.list.concat(newList) })
                });
                break
        } 
    }

    render () {
        // const list = [this.props.newPapers, this.props.hotPapers, this.props.recommendPapers]
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
                    <ScrollView
                    scrollY
                    scrollWithAnimation
                    scrollTop='0'
                    // lowerThreshold='10'
                    // upperThreshold='10'
                    style={{ height: getWindowHeight() }}
                    // onScrollToUpper={this.updateList}
                    onScrollToLower={this.fetchNextData.bind(this,this.state.current)}
                    >
                        { this.state.loaded && <PaperList list={this.state.list} /> }
                        { this.state.loading && <Loading /> }
                    </ScrollView>

            </View>
        )
    }
}

export default Home