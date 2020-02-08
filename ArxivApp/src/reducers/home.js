/* eslint-disable no-unused-vars */
import { 
    GET_NEW_PAPER, 
    GET_HOT_PAPER, 
    GET_RECOMMEND_PAPER 
} from "../constants/home"

const defaultState = {
    // papers : []
    newPapers : [],
    hotPapers : [],
    recommendPapers : [],
  };
  
const home = (state = defaultState, action) => {
    switch (action.type) {
        case GET_NEW_PAPER:
            return { ...state, newPapers: state.newPapers = action.papers };
        case GET_HOT_PAPER:
            return { ...state, hotPapers: state.hotPapers = action.papers };
        case GET_RECOMMEND_PAPER:
            return { ...state, recommendPapers: state.recommendPapers = action.papers };
        default:
            return state;
    }
};
    
export default home;