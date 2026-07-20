<script setup>

import { ref } from 'vue'
import axios from 'axios'


// 用户输入
const input = ref("")


// AI回答
const answer = ref("")


// 当前模式
const mode = ref("chat")


// 加载状态
const loading = ref(false)



async function sendMessage(){


  if(!input.value.trim()){
    return
  }


  loading.value = true

  answer.value = "AI正在分析..."



  try{


    // 普通问答模式

    if(mode.value === "chat"){


      const res = await axios.post(
        "http://127.0.0.1:8000/chat",
        {

          message: input.value

        }
      )


      answer.value = res.data.answer


    }


    // 写作模式

    else{


      const res = await axios.post(

        "http://127.0.0.1:8000/write",

        {

          content_type: mode.value,

          game_info: input.value,

          user_level:"新手"

        }

      )


      answer.value = res.data.content


    }



  }catch(error){


    console.log(error)

    answer.value =
    "请求失败，请检查后端是否启动"



  }


  loading.value=false


}



</script>



<template>


<div class="container">


<h1>
🎮 GameSense AI
</h1>


<p>
AI 游戏攻略助手
</p>



<!-- 模式选择 -->

<div class="mode">


<label>
选择功能：
</label>


<select v-model="mode">


<option value="chat">
普通攻略问答
</option>


<option value="xiaohongshu">
小红书攻略生成
</option>


<option value="video">
B站视频脚本
</option>


<option value="review">
游戏测评文章
</option>


</select>


</div>




<!-- 输入框 -->


<textarea

v-model="input"

placeholder="例如：黑神话悟空虎先锋怎么打？"

>


</textarea>




<button

@click="sendMessage"

:disabled="loading"

>

{{loading?"生成中...":"发送"}}

</button>





<!-- 输出 -->


<div class="result">


<h3>
AI结果：
</h3>


<pre>
{{answer}}
</pre>


</div>



</div>


</template>





<style scoped>


.container{

width:800px;

margin:40px auto;

font-family:
Arial,
"Microsoft YaHei";

}



h1{

text-align:center;

}



.mode{

margin:20px 0;

}



select{

padding:8px;

font-size:16px;

}



textarea{


width:100%;

height:150px;

padding:15px;

font-size:16px;

}



button{


margin-top:20px;

padding:12px 30px;

font-size:16px;

cursor:pointer;

}



.result{


margin-top:30px;

padding:20px;

border-radius:10px;

background:#f5f5f5;


}



pre{


white-space:pre-wrap;

font-size:16px;

line-height:1.6;

}



</style>