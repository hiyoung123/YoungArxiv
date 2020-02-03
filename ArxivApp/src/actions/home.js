/* eslint-disable import/prefer-default-export */
/* eslint-disable no-unused-vars */
import API from "../service/api"
import { 
  GET_NEW_PAPER, 
  GET_HOT_PAPER, 
  GET_RECOMMEND_PAPER 
} from "../constants/home"

export const getNewPapers = () => {
    return async dispatch => {
        let result = await API.get("posts/");
        dispatch({
          type: GET_NEW_PAPER,
          papers: result
        });
      };
  };

export const getHotPapers = () => {
  return async dispatch => {
      let result = await API.get("comments/");
      dispatch({
        type: GET_HOT_PAPER,
        papers: result
      });
    };
};

export const getRecommendPapers = () => {
  return async dispatch => {
      let result = await API.get("profile/");
      dispatch({
        type: GET_RECOMMEND_PAPER,
        papers: result
      });
    };
};