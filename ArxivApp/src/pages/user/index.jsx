import Taro, { Component }from '@tarojs/taro'
import { View } from '@tarojs/components'

export default class User extends Component {

    config = {
        navigationBarTitleText : "我的  "
    }

    goToPage(){
        // if (!this.props.access_token) {
          Taro.navigateTo({
            url: '/pages/login/index',
          });
          return;
        // }
        // Taro.navigateTo({
        //   url: e.currentTarget.dataset.url,
        // });
      };

    render () {
        const { mobile, coupon_number, nickname, list } = this.props;
        return (
            <View>
                <View 
                  data-url='/pages/login/index'
                  onClick={this.goToPage.bind(this)}
                >
                    <View className={mobile ? 'name black' : 'name '}>
                        {nickname || '请登录 >'}
                    </View>
                </View>
            </View>
        )
    }
}