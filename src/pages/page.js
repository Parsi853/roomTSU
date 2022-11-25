import React from "react";
import './page.sass';

const Page= ({img,title})=>{
return (
    <main className="content" style={
        {backgroundImage:"url('"+img+"')"}
    }>
    <h1 className='title'>{title} </h1>
    </main>     
)
}
export default Page