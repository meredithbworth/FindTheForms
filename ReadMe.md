# Pinwheel Coding Challenge: Find the Forms!

- Taking a list of tax form names (ex: "Form W-2", "Form 1095-C"), search the website and return some
  informational results. Specifically, you must return the "Product Number", the "Title", and the maximum and
  minimum years the form is available for download. The forms returned should be an exact match for the input (ex:
  "Form W-2" should not return "Form W-2 P", etc.) The results should be returned as json,

- Taking a tax form name (ex: "Form W-2") and a range of years (inclusive, 2018-2020 should fetch three
  years), download all PDFs available within that range. The forms returned should be an exact match for the input
  (ex: "Form W-2" should not return "Form W-2 P", etc.) The downloaded PDFs should be downloaded to a
  subdirectory under your script's main directory with the name of the form, and the file name should be the "Form
  Name - Year" (ex: Form W-2/Form W-2 - 2020.pdf)
