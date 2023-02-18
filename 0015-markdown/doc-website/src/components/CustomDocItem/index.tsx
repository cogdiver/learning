import React from 'react';
import ActualDocItem from '@theme/DocItem';
import styles from "./styles.module.scss";

const CustomDocItem = (props) => (
  <div className={`custom_doc_item_wrapper ${styles["custom_doc_item_wrapper"]}`}>
    <ActualDocItem {...props} />
  </div>
)

export default CustomDocItem;
