
SELECT [F1]
      ,[Id]
      ,[EmployeeName]
      ,[JobTitle]
      ,[BasePay]
      ,[OvertimePay]
      ,[OtherPay]
      ,[Benefits]
      ,[TotalPay]
      ,[TotalPayBenefits]
      ,[Year]
      ,[Agency]
      ,[Status]
  FROM [salaris].[dbo].['sf salaries$']

  SELECT
	id,
	EmployeeName,
	JobTitle,
	TotalPay
  From
	[salaris].[dbo].['sf salaries$']
WHERE
	TotalPay = (
		SELECT
			MAX(TotalPay)

		FROM
			[salaris].[dbo].['sf salaries$']
	);
	SELECT
	id,
	EmployeeName,
	JobTitle,
	TotalPay
  From
	[salaris].[dbo].['sf salaries$']
WHERE
	TotalPay = (
		SELECT
			Min(TotalPay)
		FROM
			[salaris].[dbo].['sf salaries$']
			);

SELECT EmployeeName , TotalPay
FROM     ['sf salaries$']
WHERE    TotalPay > (SELECT AVG(TotalPay)
FROM     ['sf salaries$']);

SELECT [Year] , TotalPay
FROM     ['sf salaries$']
WHERE    TotalPay > (SELECT AVG(TotalPay)
FROM     ['sf salaries$']);

SELECT TotalPay , JobTitle
FROM     ['sf salaries$']
WHERE    TotalPay > (SELECT AVG(TotalPay)
FROM     ['sf salaries$']);

SELECT JobTitle,                       
SUM(TotalPay)                        
FROM ['sf salaries$']                     
GROUP BY JobTitle; 



	 SELECT
	JobTitle,
	TotalPayBenefits
  From
	[salaris].[dbo].['sf salaries$']
WHERE
	TotalPay = (
		SELECT
			MAX(TotalPayBenefits)

		FROM
			[salaris].[dbo].['sf salaries$'])

SELECT OvertimePay , TotalPayBenefits
FROM     ['sf salaries$']
WHERE    OvertimePay > (SELECT count(OvertimePay)
FROM     ['sf salaries$']);