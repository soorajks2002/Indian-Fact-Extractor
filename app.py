import streamlit as st
import re
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def get_regex (inp) :
  phn_3 = re.findall("[0-9]{3}[ -][0-9]{3}[ -][0-9]{4}", inp)
  phn_10 = re.findall("[0-9]{10}", inp)
  email = re.findall("[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+", inp)
  website = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", inp)

  return phn_3, phn_10, email, website

def get_names(text) :
  names = []
  nltk_results = ne_chunk(pos_tag(word_tokenize(text)))
  for nltk_result in nltk_results:
    if type(nltk_result) == Tree:
      if nltk_result.label() == 'PERSON' :
        name = ''
        for nltk_result_leaf in nltk_result.leaves():
          name += nltk_result_leaf[0] + ' '
          names.append(name)
  return names


st.title("Feature Extractor")

inp = st.text_area("Enter Text")

if inp :
    p1, p2, e, w = get_regex(inp)
    na = get_names(inp)
    
    if p1 :
        for i in p1 :
            phone = "Phone : " + i
            st.success(phone)
        
    if p2 :
        for i in p2 :
            phone = "Phone : " + i
            st.success(phone)
            
    if e :
        for i in e :
            email = "E-Mail : " + i
            st.error(email)
            
    if w :
        for i in w :
            website = "Website : " + i
            st.warning(website)
            
    if na :
        for i in na :
            name = "Name : " + i
            st.info(name)