
const getHtml = async () => {
  try {
    return await axios.get("https://jasoseol.com/recruit");
  } catch (error) {
    console.error(error);
  }
};

getHtml()
.then(res => {
    console.log(res.data);
    console.log(res.data.split("<div").filter((el) => el.includes("calendar-right"))); // 요런식으로 끄내면 된다잉
})
