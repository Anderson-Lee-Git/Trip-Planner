import React, { useState } from 'react'
import { Stack, IconButton, Button } from '@mui/material';
import {Add} from "@mui/icons-material"
//import EventList from "../Components/TripPage/EventList"
//import Member from "../Components/TripPage/Member"
//import {sample_package_data} from "../DummyInfo/sample_package_data"
import {sample_transaction_list} from "../DummyInfo/sample_transaction_list"

function TransactionSheet(props) { // props = list element in sample data?
  console.log(props)
  let payer = sample_transaction_list[props.payer_name]
  return (
    <div>{payer}</div>
  )
}

export default TransactionSheet