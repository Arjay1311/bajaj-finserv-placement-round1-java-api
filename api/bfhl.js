const express = require("express");
const app = express();

app.use(express.json());

app.post("/api/bfhl", (req, res) => {
  const data = req.body.data || [];

  const user_id = "arjay_jg_13112004";
  const email = "arjayjg1311@gmail.com";
  const college_roll_number = "22BCE1510";

  const arr_of_even_numbers = data.filter(
    (i) => !isNaN(i) && Number.isInteger(Number(i)) && Number(i) % 2 === 0
  );

  const arr_of_odd_numbers = data.filter(
    (i) => !isNaN(i) && Number.isInteger(Number(i)) && Number(i) % 2 !== 0
  );

  const alphabets = data.filter(
    (i) => i.length === 1 && ((i >= "a" && i <= "z") || (i >= "A" && i <= "Z"))
  );

  const arr_of_special_characters = data.filter(
    (i) =>
      i.length === 1 &&
      !(
        (i >= "0" && i <= "9") ||
        (i >= "a" && i <= "z") ||
        (i >= "A" && i <= "Z")
      )
  );

  const sum_of_numbers = data
    .filter((i) => !isNaN(i) && Number.isInteger(Number(i)))
    .reduce((sum, n) => sum + Number(n), 0)
    .toString();

  const concat_string = alphabets.join("").split("").reverse().join("");


  const response = {
    is_success: "true",
    user_id,
    email,
    college_roll_number,
    even_numbers: arr_of_even_numbers,
    odd_numbers: arr_of_odd_numbers,
    alphabets,
    special_characters: arr_of_special_characters,
    sum_of_numbers,
    concat_string
  };

  res.json(response);
});


module.exports = app;
