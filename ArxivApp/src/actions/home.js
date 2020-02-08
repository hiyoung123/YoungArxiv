/* eslint-disable import/prefer-default-export */
/* eslint-disable no-unused-vars */
import API from "../service/api"
import { 
  GET_NEW_PAPER, 
  GET_HOT_PAPER, 
  GET_RECOMMEND_PAPER 
} from "../constants/home"

const defaultPayload = {
  start: 0,
  size: 10
}

export const getNewPapers = (payload=defaultPayload) => {
    return async dispatch => {
        let result = await API.get("news/?_start="+payload.start+"&_limit="+payload.size);
        dispatch({
          type: GET_NEW_PAPER,
          papers: result
        });
      };
  };

export const getHotPapers = (payload=defaultPayload) => {
  return async dispatch => {
      let result = await API.get("hots/?_start="+payload.start+"&_limit="+payload.size);
      dispatch({
        type: GET_HOT_PAPER,
        papers: result
      });
    };
};

export const getRecommendPapers = (payload=defaultPayload) => {
  return async dispatch => {
      let result = await API.get("recommends/?_start="+payload.start+"&_limit="+payload.size);
      dispatch({
        type: GET_RECOMMEND_PAPER,
        papers: result
      });
    };
};