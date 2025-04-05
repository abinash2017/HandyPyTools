GO
CREATE TABLE [dbo].[Passwords](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[password_creation] [varchar](255) NULL,
	[time_created] [varchar](255) NULL,
	[use_for_application] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

