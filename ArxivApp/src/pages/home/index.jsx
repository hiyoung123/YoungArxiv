/* eslint-disable react/jsx-closing-bracket-location */
/* eslint-disable no-unused-vars */
/* eslint-disable react/jsx-indent-props */
/* eslint-disable react/no-unused-state */
import Taro, { Component }from '@tarojs/taro'
import { View } from '@tarojs/components'
import { AtTabBar, AtList, AtListItem } from "taro-ui"
import { connect } from '@tarojs/redux'
import FakeSearchBar from "../../components/fake-search-bar";
import URL from "../../constants/urls";
import { 
    getNewPapers,
    getHotPapers,
    getRecommendPapers
 } from "../../actions/home"

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
        console.log(type)
        switch(type){
            case 0:
                this.props.dispatchGetNewPapers();
                break
            case 1:
                this.props.dispatchGetHotPapers();
                break
            case 2:
                this.props.dispatchGetRecommendPapers();
                break
        } 
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
                <View>              
                    <AtList>
                        {this.props.papers.map(item => 
                                <AtListItem
                                title={item.title}
                                note={item.author}
                                arrow='right'
                                thumb='http://img12.360buyimg.com/jdphoto/s72x72_jfs/t10660/330/203667368/1672/801735d7/59c85643N31e68303.png'
                            />
                        )}
                    </AtList> 
                </View>
            </View>
        )
    }
}

export default Home