/* eslint-disable no-unused-vars */
import { GET_NEW_PAPER } from "../constants/home"

const defaultState = {
    newPapers : [],
  };
  
const home = (state = defaultState, action) => {
    switch (action.type) {
        case GET_NEW_PAPER:
            return { ...state, newPapers: state.newPapers.concat(action.papers) };
        default:
            return state;
    }
};
    
export default home;